# Prompt Hub — Schema Discovery Report

**Date:** 2026-04-18
**Project:** ALIGN (Supabase `ojrswncqntvyoorgdyen`)
**Scope:** Discovery only — no rows written or modified.

> Note on file location: the task spec requested `~/Documents/alignai-prompt-hub-audit/…`. That path sits on Craig's machine and is outside this sandbox. Report was saved inside the selected workspace (`alignai-prompts/audit/`) so you can see it. Move or symlink locally as needed.

---

## 1. Prompt-related tables and row counts

| Table / View | Kind | Rows |
|---|---|---|
| `prompt_hub_prompts` | table | 92 |
| `prompt_hub_variants` | table | 368 |
| `prompt_categories` | table | 19 |
| `prompt_requests` | table | 0 |
| `prompt_hub_searches` | table | (not profiled — not touched by audit) |
| `prompt_hub_signups` | table | (not profiled — not touched by audit) |
| `v_prompt_catalog` | view | one row per published prompt + category + variant_count |
| `v_prompt_hub_stats` | view | per-category aggregates |
| `v_prompt_variants_full` | view | one row per published prompt × variant (this is what `build.py` reads) |
| `v_stale_variants` | view | freshness labels (fresh / aging / stale / never_verified) |

> Heads-up: live counts are higher than the `prompts.alignai.business` project context doc. Context says **74 prompts / 296 variants**; Supabase says **92 prompts / 368 variants**. Four models × 92 prompts = 368 checks out. Context doc should be updated after this audit concludes.

---

## 2. Column schemas

### `prompt_hub_prompts` (master prompt record)

```
id               integer        PK, serial
title            varchar        not null
slug             varchar        not null
category_id      integer        not null → prompt_categories.id
status           varchar        default 'published'
difficulty       varchar        not null        (Beginner / Intermediate / Expert)
prompt_style     varchar        not null        (Zero-shot / Few-shot / Agentic / …)
business_value   varchar        not null        (Revenue-driving / Time-saving / …)
use_case         text
pro_tip          text
tags             text[]
related_tool_slugs text[]
featured         boolean        default false
sort_order       integer        default 0
view_count       integer        default 0
search_vector    tsvector
created_at       timestamptz    default now()
updated_at       timestamptz    default now()
```

### `prompt_hub_variants` (per-model prompt body — the audit target)

```
id                integer        PK, serial
prompt_id         integer        not null → prompt_hub_prompts.id
model_name        varchar        not null        (Claude / ChatGPT / Gemini / Copilot)
prompt_text       text           not null
notes             text                           (per-model usage tip shown next to the prompt body)
model_version     varchar                        (free text: "Claude 4.x", "GPT-5", "Gemini 3 Pro", "Copilot for M365")
last_verified_at  timestamptz                    (drives the fresh / aging / stale badge)
copy_count        integer        default 0
created_at        timestamptz    default now()
updated_at        timestamptz    default now()
```

**Audit-critical observation.** `prompt_hub_variants` has **no** `status`, `is_active`, `is_draft`, `published_at`, `superseded_by`, or `parent_variant_id` column. No versioning mechanism exists today.

### `prompt_categories`

```
id / name / slug / description / icon / sort_order / created_at / updated_at
```

### `prompt_requests` (inbound prompt request form — currently empty)

```
id / email / supabase_user_id / request_text / category_hint / status / built_prompt_id / created_at / updated_at
```

---

## 3. How the live site renders variants (critical for draft safety)

`build.py` calls `supabase.table("v_prompt_variants_full").select("*")` and hands every row to the Jinja template `templates/prompt.html`, which renders **one tab per unique `model_name`** in the returned set.

View definition (abridged):

```sql
SELECT p.id AS prompt_id, p.title, p.slug AS prompt_slug,
       c.name AS category, p.difficulty, p.prompt_style, p.business_value,
       pv.model_name, pv.prompt_text, pv.notes AS model_notes,
       pv.model_version, pv.last_verified_at, pv.copy_count,
       p.pro_tip, p.tags, p.view_count
FROM prompt_hub_prompts p
JOIN prompt_categories c ON c.id = p.category_id
JOIN prompt_hub_variants pv ON pv.prompt_id = p.id
WHERE p.status = 'published'   -- prompt-level filter only
ORDER BY p.id, pv.model_name;
```

**Implication.** The view filters on the prompt's `status`, not the variant's. If I insert a new row in `prompt_hub_variants` for a published prompt — even with a non-standard `model_name` like `"Claude (Draft)"` — it will immediately appear on `prompts.alignai.business` on the next static build. There is no place to mark a row as "draft" today.

---

## 4. Variant breakdown

### Variants per `model_name`

| model_name | variants | distinct model_versions |
|---|---|---|
| ChatGPT | 92 | 1 (`GPT-5`) |
| Claude | 92 | 1 (`Claude 4.x`) |
| Copilot | 92 | 2 |
| Gemini | 92 | 2 |

### Claude subset (the audit set)

- **Claude variants to audit:** 92 (one per published prompt)
- **Distinct model_version:** `Claude 4.x` on every row
- **Oldest `last_verified_at`:** 2026-04-12 18:47:22 UTC
- **Newest `last_verified_at`:** 2026-04-15 00:00:00 UTC
- **Avg prompt length:** 1,865 chars
- **Max prompt length:** 5,179 chars

---

## 5. Sample rows (one per table, sensitive fields redacted)

### `prompt_hub_variants` — id=1 (Claude variant of "SEO Content Brief Generator")

```
id:                1
prompt_id:         1
model_name:        Claude
model_version:     Claude 4.x
last_verified_at:  2026-04-12 18:47:22+00
copy_count:        0
prompt_text (first 200 chars):
  "You are an SEO content strategist for small businesses. Generate
   a comprehensive content brief for a blog post targeting the keyword
   \"[TARGET_KEYWORD]\" for a [INDUSTRY] business. Include: 1. Three ti…"
notes (first 120 chars):
  "Claude excels at structured, detailed output. Use XML tags — wrap
   your context in <business_context> tags for cleaner re…"
```

### `prompt_hub_prompts` — id=1

```
id: 1 | title: SEO Content Brief Generator | slug: seo-content-brief-generator
category_id: 1 | status: published | difficulty: Beginner
prompt_style: Zero-shot | business_value: Revenue-driving
use_case: "Generate a structured SEO content brief for a blog post targeting a specific keyword, including title options, meta desc…"
featured: false | view_count: 0
```

### `prompt_hub_prompts` — id=3 (Expert / Agentic example)

```
id: 3 | title: AI-Powered Lead Qualification & Scoring
slug: ai-powered-lead-qualification-scoring
difficulty: Expert | prompt_style: Agentic | business_value: Revenue-driving
```

---

## 6. Does a status / draft mechanism exist?

**No.** Full check: no column named `status`, `state`, `is_active`, `is_draft`, `published_at`, `superseded_by`, or `parent_variant_id` exists on `prompt_hub_variants`. No sibling table like `prompt_hub_variant_drafts`. No `archived_at` soft-delete column.

The only "versioning-ish" field today is `last_verified_at`, which drives the freshness badge (`v_stale_variants`: `fresh` / `aging` / `stale` / `never_verified`).

---

## 7. Recommendation for the versioning mechanism

Because the view pipes every variant row straight to the public site, a "naming convention" approach (e.g. prefix `model_name` with `DRAFT-`) is unsafe — it would create a new Claude-like tab on the live site. We need real variant-level filtering.

Minimal viable migration (single `ALTER TABLE` + single view replace). Proposed:

```sql
ALTER TABLE prompt_hub_variants
  ADD COLUMN status            varchar      NOT NULL DEFAULT 'active',
  ADD COLUMN parent_variant_id integer      REFERENCES prompt_hub_variants(id),
  ADD COLUMN audit_source      varchar,
  ADD COLUMN superseded_by     integer      REFERENCES prompt_hub_variants(id);

CREATE INDEX idx_variants_status ON prompt_hub_variants(status);

-- Update the view so only 'active' rows render on the live site
CREATE OR REPLACE VIEW v_prompt_variants_full AS
  SELECT p.id AS prompt_id, p.title, p.slug AS prompt_slug,
         c.name AS category, c.slug AS category_slug,
         p.difficulty, p.prompt_style, p.business_value,
         pv.model_name, pv.prompt_text, pv.notes AS model_notes,
         pv.model_version, pv.last_verified_at, pv.copy_count,
         p.pro_tip, p.tags, p.view_count
  FROM prompt_hub_prompts p
  JOIN prompt_categories c ON c.id = p.category_id
  JOIN prompt_hub_variants pv ON pv.prompt_id = p.id
  WHERE p.status = 'published'
    AND pv.status = 'active'        -- NEW FILTER
  ORDER BY p.id, pv.model_name;
```

Status values this supports:
- `active` — current live variant (backfill all 368 existing rows to this)
- `draft` — audit-produced draft awaiting Craig's review (invisible to build.py)
- `archived` — previous variant kept for history after being superseded

Draft insert pattern this enables:

```sql
INSERT INTO prompt_hub_variants
  (prompt_id, model_name, prompt_text, notes, model_version,
   status, parent_variant_id, audit_source)
VALUES
  (1, 'Claude', '<optimized body>', '<notes>', 'Claude 4.x',
   'draft', 1, 'opus-4-7-audit-2026-04-18');
```

Admin activation (done by Craig, one at a time, after review):

```sql
BEGIN;
UPDATE prompt_hub_variants SET status = 'archived', superseded_by = <draft_id> WHERE id = <parent_id>;
UPDATE prompt_hub_variants SET status = 'active',   last_verified_at = now()   WHERE id = <draft_id>;
COMMIT;
```

Risk on this migration: none for reads (view stays public-compatible). The only write-path risk is any direct INSERT code that doesn't set `status` — `DEFAULT 'active'` absorbs that.

### Alternatives considered and ruled out

- **Naming-convention (`model_name = 'Claude (Draft)'`)** — creates a new tab on the live site. Unsafe.
- **Use `notes` field prefix** — still published; still rendered. Unsafe.
- **New `prompt_hub_variant_drafts` table** — cleaner separation but duplicates all the downstream machinery (v_stale_variants, freshness logic, admin UI, activation SQL). Higher blast radius for small gain.
- **Dry-run JSON-only output, no Supabase writes** — would be safest but breaks Craig's stated workflow of activating drafts in the admin UI.

---

## 8. Counts headed into Step 3

- **Total Claude variants to audit:** 92
- **Table to write drafts to:** `prompt_hub_variants` (same table, new rows with `status='draft'`)
- **Audit tag to apply on every insert:** `audit_source = 'opus-4-7-audit-2026-04-18'`
- **Estimated OPTIMIZE rate (rough prior, pre-audit):** 30–50% of 92, call it ~30–45 variants needing side-by-side API tests on `claude-opus-4-7`

---

## 9. Questions for Craig (the Step 1 pause)

Please answer all three before I proceed to Step 2.

**Q1. Audit set confirmed?**
92 rows in `prompt_hub_variants` where `model_name = 'Claude'` and `model_version = 'Claude 4.x'`, one per published prompt. Target table: `prompt_hub_variants`. YES / NO.

**Q2. Versioning mechanism?**
My recommendation is the minimal migration in §7 (add `status` + `parent_variant_id` + `audit_source` + `superseded_by`; backfill existing rows to `status='active'`; update `v_prompt_variants_full` to filter `pv.status = 'active'`). This is the only approach I found that lets me write drafts without them leaking to the live site. Options:

- **A.** Proceed with the recommended migration (I'll run it as a proper `apply_migration` — one `ALTER TABLE` + one `CREATE OR REPLACE VIEW` + a backfill `UPDATE`).
- **B.** You have a different versioning scheme in mind (describe it).
- **C.** Skip writes entirely — produce the audit as markdown only, and you'll paste approved changes into the admin UI by hand.

**Q3. Batch size?**
- **Full run** — audit all 92 in one pass, write all drafts at the end.
- **Batched** — 20 at a time, I pause and show you the classification breakdown between batches so you can course-correct the rules.

---

## 10. What has NOT been done

No rows written. No rows modified. No migrations applied. No API calls to `claude-opus-4-7`. All queries above were read-only `SELECT`s against `information_schema` and the four prompt tables.

**Waiting on Craig's three answers before proceeding to Step 2.**
