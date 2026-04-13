#!/usr/bin/env python3
"""
AlignAI Prompt Hub — Static Site Generator
Connects to Supabase, fetches prompt data, and generates static HTML via Jinja2.
Output: dist/ directory with index.html, category/*/index.html, prompts/*/index.html
"""

import os
import sys
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    sys.exit("ERROR: jinja2 not installed. Run: pip install jinja2")

try:
    from supabase import create_client, Client
except ImportError:
    sys.exit("ERROR: supabase not installed. Run: pip install supabase")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
DIST_DIR = BASE_DIR / "dist"

SITE_URL = "https://prompts.alignai.business"
SITE_NAME = "AlignAI Prompt Hub"
OG_IMAGE = f"{SITE_URL}/assets/og-image.png"


# ---------------------------------------------------------------------------
# Supabase helpers
# ---------------------------------------------------------------------------

def get_supabase_client() -> Client:
    """Create Supabase client from environment variables."""
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        sys.exit("ERROR: SUPABASE_URL and SUPABASE_KEY environment variables are required.")
    return create_client(url, key)


def fetch_data(supabase: Client) -> dict:
    """Fetch all views needed for the static build."""
    print("Fetching data from Supabase...")

    # v_prompt_catalog -- one row per prompt with category info
    catalog_resp = supabase.table("v_prompt_catalog").select("*").execute()
    catalog = catalog_resp.data or []
    print(f"  v_prompt_catalog: {len(catalog)} rows")

    # v_prompt_hub_stats -- aggregate stats per category + totals
    stats_resp = supabase.table("v_prompt_hub_stats").select("*").execute()
    stats = stats_resp.data or []
    print(f"  v_prompt_hub_stats: {len(stats)} rows")

    # v_prompt_variants_full -- one row per prompt x model variant
    variants_resp = supabase.table("v_prompt_variants_full").select("*").execute()
    variants = variants_resp.data or []
    print(f"  v_prompt_variants_full: {len(variants)} rows")

    return {
        "catalog": catalog,
        "stats": stats,
        "variants": variants,
    }


# ---------------------------------------------------------------------------
# Freshness computation
# ---------------------------------------------------------------------------

def compute_freshness(last_verified_at: Optional[str]) -> Tuple[str, str]:
    """
    Returns (freshness_class, display_date) tuple.

    freshness_class: 'fresh' (<=30 days), 'aging' (31-90), 'stale' (91+ or NULL)
    display_date: label + date string, e.g. 'FRESH APR 2026' or 'UNVERIFIED'
    """
    if not last_verified_at:
        return ("stale", "UNVERIFIED")

    # Parse the timestamp
    if isinstance(last_verified_at, str):
        verified = datetime.fromisoformat(last_verified_at.replace("Z", "+00:00"))
    else:
        verified = last_verified_at

    # Ensure timezone-aware
    if verified.tzinfo is None:
        verified = verified.replace(tzinfo=timezone.utc)

    now = datetime.now(timezone.utc)
    days_ago = (now - verified).days
    month_year = verified.strftime("%b %Y").upper()  # e.g. "APR 2026"

    if days_ago <= 30:
        return ("fresh", "FRESH " + month_year)
    elif days_ago <= 90:
        return ("aging", "UPDATED " + month_year)
    else:
        return ("stale", "AGING " + month_year)


# ---------------------------------------------------------------------------
# Category short labels
# ---------------------------------------------------------------------------

def make_short_label(category_name: str) -> str:
    """
    Derive a short uppercase monospace label from the category name.
    Uses the first word, uppercased. Override specific names for clarity.
    """
    overrides = {
        "marketing & sales": "MARKETING",
        "marketing and sales": "MARKETING",
        "operations & logistics": "OPERATIONS",
        "operations and logistics": "OPERATIONS",
        "customer service": "SUPPORT",
        "customer support": "SUPPORT",
        "finance & strategy": "FINANCE",
        "finance and strategy": "FINANCE",
        "human resources": "PEOPLE",
        "hr": "PEOPLE",
    }
    lower = category_name.strip().lower()
    if lower in overrides:
        return overrides[lower]
    # Default: first word uppercased
    first_word = category_name.strip().split()[0] if category_name.strip() else "OTHER"
    return first_word.upper()


# ---------------------------------------------------------------------------
# Friendly style labels
# ---------------------------------------------------------------------------

def friendly_style(style: Optional[str]) -> Optional[str]:
    """
    Map technical prompt-style names to plain English labels.
    Used on the prompt detail page badges.
    """
    if not style:
        return None
    mapping = {
        "Zero-shot": "PASTE & GO",
        "zero-shot": "PASTE & GO",
        "Few-shot": "ADD YOUR EXAMPLES",
        "few-shot": "ADD YOUR EXAMPLES",
        "Chain-of-thought": "STEP BY STEP",
        "chain-of-thought": "STEP BY STEP",
        "Agentic": "MULTI-STEP WORKFLOW",
        "agentic": "MULTI-STEP WORKFLOW",
    }
    return mapping.get(style, style.upper())


# ---------------------------------------------------------------------------
# Data organisation helpers
# ---------------------------------------------------------------------------

def organise(data: dict) -> dict:
    """
    Transform raw Supabase rows into structures the templates expect.
    Returns a dict with keys: categories, prompts, variants_by_prompt,
    category_stats, totals.
    """
    catalog = data["catalog"]
    stats = data["stats"]
    variants = data["variants"]

    # --- Category stats (from v_prompt_hub_stats) --------------------------
    category_stats: dict = {}
    for row in stats:
        slug = row.get("category_slug") or row.get("slug")
        if slug:
            category_stats[slug] = row

    # --- Build unique category list from catalog --------------------------
    categories: dict = {}
    for row in catalog:
        cat_slug = row.get("category_slug")
        if not cat_slug:
            continue
        if cat_slug not in categories:
            cat_name = row.get("category_name") or cat_slug
            categories[cat_slug] = {
                "slug": cat_slug,
                "name": cat_name,
                "description": row.get("category_description", ""),
                "short_label": make_short_label(cat_name),
                "prompt_count": category_stats.get(cat_slug, {}).get("prompt_count", 0),
            }

    # --- Prompts list & lookup by slug ------------------------------------
    prompts: dict = {}
    for row in catalog:
        slug = row.get("slug")
        if not slug:
            continue
        prompts[slug] = row

    # --- Variants grouped by prompt slug ----------------------------------
    # Also compute freshness for each variant
    variants_by_prompt: dict = {}
    for v in variants:
        freshness_class, freshness_date = compute_freshness(v.get("last_verified_at"))
        v["freshness_class"] = freshness_class
        v["freshness_date"] = freshness_date

        ps = v.get("prompt_slug")
        if ps:
            variants_by_prompt.setdefault(ps, []).append(v)

    # --- Prompts grouped by category slug ---------------------------------
    prompts_by_category: dict = {}
    for p in catalog:
        cs = p.get("category_slug")
        if cs:
            prompts_by_category.setdefault(cs, []).append(p)

    # --- Featured prompts -------------------------------------------------
    featured = [p for p in catalog if p.get("featured")]

    # --- Totals -----------------------------------------------------------
    total_prompts = len(prompts)
    total_variants = len(variants)
    total_categories = len(categories)

    return {
        "categories": categories,
        "prompts": prompts,
        "prompts_by_category": prompts_by_category,
        "variants_by_prompt": variants_by_prompt,
        "featured": featured,
        "totals": {
            "total_prompts": total_prompts,
            "total_variants": total_variants,
            "total_categories": total_categories,
        },
    }


# ---------------------------------------------------------------------------
# Jinja2 helpers
# ---------------------------------------------------------------------------

def truncate_text(text: str, length: int = 200) -> str:
    """Truncate text to *length* characters, adding ellipsis if needed."""
    if not text:
        return ""
    if len(text) <= length:
        return text
    return text[:length].rsplit(" ", 1)[0] + "..."


def prompt_preview(text: str, pct: float = 0.20, max_chars: int = 200) -> str:
    """Return the first ~20 % of prompt_text (capped at max_chars)."""
    if not text:
        return ""
    target = min(int(len(text) * pct), max_chars)
    if target >= len(text):
        return text
    return text[:target].rsplit(" ", 1)[0] + "..."


def difficulty_color(difficulty: Optional[str]) -> str:
    """Return CSS class for difficulty badge."""
    mapping = {
        "beginner": "badge-beginner",
        "intermediate": "badge-intermediate",
        "expert": "badge-expert",
    }
    return mapping.get((difficulty or "").lower(), "badge-beginner")


def get_jinja_env() -> Environment:
    """Create and configure the Jinja2 environment."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    # Custom filters
    env.filters["truncate_text"] = truncate_text
    env.filters["prompt_preview"] = prompt_preview
    env.filters["difficulty_color"] = difficulty_color

    # Global constants available in every template
    env.globals["SITE_URL"] = SITE_URL
    env.globals["SITE_NAME"] = SITE_NAME
    env.globals["OG_IMAGE"] = OG_IMAGE

    return env


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def write_page(path: Path, html: str) -> None:
    """Write rendered HTML to *path*, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def build_index(env: Environment, ctx: dict) -> None:
    """Generate dist/index.html -- the Hub home page."""
    # Compute audit date as current month/year at build time
    site_audit_date = datetime.now(timezone.utc).strftime("%b %Y")

    tpl = env.get_template("index.html")
    html = tpl.render(
        page_title="AI Prompts That Actually Work for Small Business",
        page_description="Copy-paste prompts optimized for Claude, ChatGPT, Gemini & Copilot. Built by AlignAI.",
        canonical_url=SITE_URL,
        categories=ctx["categories"],
        featured=ctx["featured"],
        site_audit_date=site_audit_date,
        **ctx["totals"],
    )
    dest = DIST_DIR / "index.html"
    write_page(dest, html)
    print(f"  + {dest.relative_to(BASE_DIR)}")


def build_category_pages(env: Environment, ctx: dict) -> int:
    """Generate dist/category/{slug}/index.html for every category."""
    tpl = env.get_template("category.html")
    site_audit_date = datetime.now(timezone.utc).strftime("%b %Y")
    count = 0
    for slug, cat in ctx["categories"].items():
        prompts = ctx["prompts_by_category"].get(slug, [])
        html = tpl.render(
            page_title=f"{cat['name']} -- AI Prompts | AlignAI",
            page_description=cat.get("description", f"AI prompts for {cat['name']}"),
            canonical_url=f"{SITE_URL}/category/{slug}/",
            category=cat,
            prompts=prompts,
            site_audit_date=site_audit_date,
        )
        dest = DIST_DIR / "category" / slug / "index.html"
        write_page(dest, html)
        count += 1
    print(f"  + {count} category pages")
    return count


def build_prompt_pages(env: Environment, ctx: dict) -> int:
    """Generate dist/prompts/{slug}/index.html for every prompt."""
    tpl = env.get_template("prompt.html")
    count = 0
    for slug, prompt in ctx["prompts"].items():
        variants = ctx["variants_by_prompt"].get(slug, [])
        # Sort variants: Claude first, then alphabetical
        model_order = {"claude": 0, "chatgpt": 1, "gemini": 2, "copilot": 3}
        variants.sort(key=lambda v: model_order.get((v.get("model_name") or "").lower(), 99))

        cat_slug = prompt.get("category_slug", "")
        cat = ctx["categories"].get(cat_slug, {})

        # Add friendly style label for detail page badge
        prompt["friendly_style"] = friendly_style(prompt.get("prompt_style"))

        # Related prompts: up to 3 others from same category, excluding current
        related = [
            p for p in ctx["prompts_by_category"].get(cat_slug, [])
            if p.get("slug") != slug
        ][:3]

        html = tpl.render(
            page_title=f"{prompt.get('title', 'Prompt')} -- AlignAI Prompt Hub",
            page_description=prompt.get("use_case", prompt.get("title", "")),
            canonical_url=f"{SITE_URL}/prompts/{slug}/",
            prompt=prompt,
            variants=variants,
            category=cat,
            related_prompts=related,
            total_prompts=ctx["totals"]["total_prompts"],
        )
        dest = DIST_DIR / "prompts" / slug / "index.html"
        write_page(dest, html)
        count += 1
    print(f"  + {count} prompt pages")
    return count


# ---------------------------------------------------------------------------
# Static assets
# ---------------------------------------------------------------------------

def copy_static() -> None:
    """Copy static/ -> dist/assets/."""
    dest = DIST_DIR / "assets"
    if dest.exists():
        shutil.rmtree(dest)
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, dest)
        print(f"  + Static assets copied to {dest.relative_to(BASE_DIR)}")
    else:
        dest.mkdir(parents=True, exist_ok=True)
        print(f"  ! No static/ directory found -- created empty {dest.relative_to(BASE_DIR)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"\n{'='*60}")
    print(f"  AlignAI Prompt Hub -- Static Build")
    print(f"{'='*60}\n")

    # 1. Connect & fetch
    supabase = get_supabase_client()
    raw_data = fetch_data(supabase)

    # 2. Organise
    ctx = organise(raw_data)
    print(
        f"\nOrganised: {ctx['totals']['total_categories']} categories, "
        f"{ctx['totals']['total_prompts']} prompts, "
        f"{ctx['totals']['total_variants']} variants\n"
    )

    # 3. Clean dist
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    # 4. Build pages
    print("Generating pages...")
    env = get_jinja_env()
    build_index(env, ctx)
    cat_count = build_category_pages(env, ctx)
    prompt_count = build_prompt_pages(env, ctx)

    # 5. Static assets
    copy_static()

    # 6. Summary
    total_pages = 1 + cat_count + prompt_count
    print(f"\n{'='*60}")
    print(f"  BUILD COMPLETE")
    print(f"  {ctx['totals']['total_categories']} categories, "
          f"{ctx['totals']['total_prompts']} prompts, "
          f"{total_pages} pages generated")
    print(f"  Output: {DIST_DIR.relative_to(BASE_DIR)}/")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
