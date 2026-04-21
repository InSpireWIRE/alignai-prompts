# Session State — 2026-04-18 (Saturday)

Reload this file at the top of tomorrow's (or any future) session if the chat thread doesn't survive.

---

## TL;DR

Drafted Reddit + LinkedIn posts around the finding: "one line of chain-of-thought prompting flattens Claude 4.7 output." Coined pattern THE REDUNDANT SCAFFOLD. Both drafts pass craig-voice 8-point check. Target: Tue 4/21 AM on r/ClaudeAI, LinkedIn same day. Two open decisions before post goes live.

---

## What's done

**API audit (Task 4 completed earlier today):** audited 92 Claude prompts from the Prompt Hub against Opus 4.7. Found 10 with the same redundant chain-of-thought scaffold line: *"Before writing, think through the [whatever] step by step."* Optimized variants written to Supabase as drafts (370-379).

**Real A/B test (Round 2, clean compare):** ran two fresh claude.ai chats on Opus 4.7 with a SOCIAL INFLUENZA cartoon prompt. Only diff between prompts: that one CoT scaffold line. Both had explicit OUTPUT FORMAT line to kill the format-ambiguity confounder from Round 1.

**Findings from Round 2:**
- Zero modals either way
- Zero preamble either way
- BUT: NEW (scaffold removed) produced measurably sharper output on every panel
- Best NEW-only lines: *"Joined ChatGPT 2 days ago"* (Panel 2 bio), *"testimonial from day 11 of being alive"* (Panel 4), *"If you have been teaching what you just learned, please sit down"* (PSA sign-off)
- Consistent with API audit finding: scaffold in = ships but blander, scaffold out = same ship quality + tighter copy

**Drafts written:**
- `social/reddit_post_redundant_scaffold_2026-04-19.md` (filename says 4-19, retarget is Tue 4-21)
- `social/linkedin_redundant_scaffold_2026-04-21.md`
- `social/round2_clean_compare_2026-04-18.md` (the side-by-side for first-comment link)
- `social/social_influenza_real_compare_2026-04-18.md` (Round 1 transcript)
- `social/honest_compare_2026-04-18.md` (Round 1 recalibration)
- `social/real_run_prompt2_output.md` (Round 1 prompt 2 real output)

**SVGs in `/mnt/uploads/`:**
- `social_influenza_five_panel_psa.svg` (Round 1 prompt 1)
- `social_influenza_cartoon.svg` (Round 2 OLD, scaffold in)
- `social_influenza.svg` (Round 2 NEW, scaffold out)

---

## What's locked

**Reddit title:** *"Optimized 10 prompts for Claude 4.7. Turns out one line was doing all the damage."*
Picked from a 5-option pitch list. Failure-first framing, specific number, teases the fix without naming it.

**Timing:** Tuesday 4/21 AM, 6-9 AM local. r/ClaudeAI peak window. Skipped Sunday 4/19 for peak timing.

**Primary sub:** r/ClaudeAI. Highest-signal audience for this finding, lowest self-promo risk since the data is the point.

**Crosspost strategy:** stagger r/PromptEngineering and r/ChatGPTPro 24-48 hours after r/ClaudeAI reception lands. Use first post to refine title for the next subs.

**LinkedIn companion:** ship same day as Reddit. Slightly different — surfaces "zero-shot chain-of-thought" terminology earlier as a credibility signal for LinkedIn audience. Same coined term, same reader-diagnostic close.

---

## What's open

**1. Hosting for first-comment links.** Need the round2 clean compare + both SVGs at linkable URLs before posting.
- Option A: GitHub gist (fastest, markdown + SVGs render inline, free)
- Option B: Prompt Hub page at prompts.alignai.business (on-brand, drives traffic back, requires build + deploy)
- Option C: Cloudflare R2 (SVGs on own permalinks for future reuse)
- My lean: Gist for fastest path, Prompt Hub for highest leverage
- DECIDE BY: Monday night

**2. LinkedIn visual.** Want a clean OLD vs NEW comparison image cut from the two SVGs? Panel 4 testimonial contrast is the sharpest single visual ("no testimonial" vs "testimonial from day 11 of being alive").
- DECIDE BY: Monday night

**3. Monday night final read-through.** Read both drafts aloud (phone-at-a-bar test). Confirm voice check still holds.

---

## Key terminology (for any edits)

- **Chain-of-thought (CoT) prompting** = the industry term for "think step by step" instructions. Coined Wei et al 2022. Both the Reddit and LinkedIn posts quote Anthropic's 4.7 docs using this exact term.
- **THE REDUNDANT SCAFFOLD** = Craig's coined pattern name for the problem (defined in-line in both posts).
- Scaffold = everyday English, works as pattern name. CoT = precise tech term for what the line IS. Both used in posts.

---

## Voice rules that applied (in case of rewrites)

- Em-dashes: 0 (period/comma/parens/line break only)
- Authority-setup phrases: 0 (no "years taught me", "after a year", etc.)
- "We": 0 (first-person "I" always)
- Tricolons: 0
- Qualifying parentheticals: 0
- Round-rhetorical numbers: 0 (92 prompts, 10 lines are real database counts)
- Fragments: 7+ on Reddit, 10+ on LinkedIn
- Coined term defined in-line on first drop
- Reader-diagnostic close: "If you run a Claude prompt library, audit it. Bet you find at least three. Mine had 10."
- Phone-at-a-bar test: both drafts read as Craig typed this while waiting for coffee

Full rules: `/mnt/.claude/skills/craig-voice/SKILL.md`

---

## File locations (for reload)

Workspace root: `alignai-prompts/` (selected folder on Craig's machine)

```
social/
├── reddit_post_redundant_scaffold_2026-04-19.md   # Reddit draft (Tue 4/21 target)
├── linkedin_redundant_scaffold_2026-04-21.md      # LinkedIn draft (Tue 4/21 target)
├── round2_clean_compare_2026-04-18.md             # Side-by-side for first-comment link
├── social_influenza_real_compare_2026-04-18.md    # Round 1 transcript
├── honest_compare_2026-04-18.md                   # Round 1 recalibration
├── real_run_prompt2_output.md                     # Round 1 prompt 2 real output
├── social_influenza_prompt_2026-04-18.md          # Long Round 1 prompt
└── social_influenza_sidebyside_2026-04-18.md      # Initial simulated side-by-side (superseded)

(SVGs in /mnt/uploads/ — may not persist outside session. Check.)
```

---

## Resume command

To resume this work in a new session, paste into Claude:

> Load `alignai-prompts/session_state_2026-04-18.md`. We're shipping the REDUNDANT SCAFFOLD Reddit + LinkedIn posts Tuesday 4/21 AM. Two decisions open: hosting and LinkedIn visual. Pick up there.

---

*Last updated: 2026-04-18 Saturday · AlignAI · craig-voice v1.0.0*
