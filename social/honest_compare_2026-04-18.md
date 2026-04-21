# Honest Compare: the two SOCIAL INFLUENZA runs you actually ran

**What this is:** a comparison of the two outputs you produced in claude.ai yesterday — corrected for the fact that these were TWO DIFFERENT PROMPTS, not the OLD/NEW scaffold A/B I originally framed.

**What this is NOT:** a test of the scaffold hypothesis. That test is running in parallel (round 2, both short prompts with explicit OUTPUT FORMAT line, only the scaffold line differing).

---

## What you actually ran

### Run 1 — the LONG prompt
Source: `/social/social_influenza_prompt_2026-04-18.md`
~70 lines. Mentions "cartoon script," "for the illustrator," includes a visual direction section.
Does **NOT** contain the scaffold line. Explicitly forbids preamble ("No 'let me think about this' preamble").
**Result:** Claude fired 2 clarification modals → you picked SVG + "your call silhouette" → rendered SVG cartoon.

### Run 2 — a SHORTER prompt
Most likely the short NEW prompt from my "path 1" instructions. ~25 lines. No visual direction section. No explicit output format line.
**Result:** Claude wrote *"Weighed preference against detailed brief, proceeded with delivery"* at the top → delivered a written script. No modals.

---

## Side by side

| Dimension | Run 1 (long prompt) | Run 2 (short prompt) |
|---|---|---|
| Prompt length | ~70 lines | ~25 lines |
| Contains "think step by step" | No | No |
| Mentions multiple output formats | Yes (script, illustrator, visual direction, SVG-like panel 5) | No |
| Explicit OUTPUT FORMAT line | No | No |
| Clarifying questions fired | 2 | 0 |
| Adaptive-thinking header | — | "Weighed preference against detailed brief, proceeded with delivery" |
| Artifact returned | Rendered SVG cartoon | Written script |
| Panels delivered | 5 | 5 |
| PSA sections delivered | All 6 + sign-off | All 6 + sign-off |
| Quality of cartoon | Excellent | Excellent |

---

## Content quality — line for line

**Panel 1 caption**
- Run 1 (SVG): *"Asked it to write an email. It did."*
- Run 2 (script): *"First exposure. Asked it to plan dinner."*
- Both land the first-honest-use beat. Run 1 is one beat shorter. Wash.

**Panel 2 caption**
- Run 1: *"Day three. Bio now reads AI Strategist."*
- Run 2: *"Symptoms appeared within 36 hours."*
- Run 2's caption is sharper — it hits the PSA's metaphor a panel early. Run 2 wins here.

**Panel 3 caption**
- Run 1: *"Posted a carousel. Mostly arrows and vibes."*
- Run 2: *"Infection spreads through carousel vector."*
- Run 1's "arrows and vibes" is the single funniest line in either output. Run 1 wins.

**Panel 4 caption**
- Run 1: *"Stripe live. 312 on waitlist. Course unbuilt."*
- Run 2: *"Final stage. Selling the cure they caught."*
- Run 2's caption is the most biting line in either output. Run 2 wins.

**PSA condition name**
- Run 1: *"Acute AI expertise syndrome (AAES)"*
- Run 2: *"Social Influenza, strain AI-1. Commonly: Prompt Fever."*
- Run 2's version leans into the cartoon's title and coins a second name. Run 2 wins.

**Symptom bullets**
- Run 1 standouts: *"Begins sentences with 'Most people don't realize...'" · "Uses 'we' to describe a solo operation." · "Quotes own tweets in replies to own tweets."*
- Run 2 standouts: *"Ring light purchased within 72 hours of first prompt." · "Pinned post features at least three fire emojis." · "References to 'my framework' inside two weeks of first login."*
- Both lists are sharp. Run 1's "quotes own tweets in replies to own tweets" is the bitingest single bullet in the pair. Call it Run 1 by a hair.

**Sign-off**
- Run 1: *"Stay curious. Stay quiet. Ship anyway."*
- Run 2: *"Stay boring. Keep building."*
- Run 2 is two words shorter, more quotable. Run 2 wins.

**Aggregate cartoon quality:** Effectively tied. Each output has ~3 lines that outperform the other. If you were picking the best individual lines from both to build a single final cartoon, you'd pull from both.

---

## What this pair actually shows

The clean takeaway here is **not** about the scaffold. It's about **prompt specificity and format ambiguity.**

The long prompt triggered clarifying questions because it mentioned multiple possible output formats in the same brief (cartoon script, illustrator brief, visual direction, SVG-style panel 5 format). Claude reasonably asked *which one do you want?*

The short prompt didn't mention any specific format. Claude picked a default (written script) and shipped.

**Counter-intuitive insight:** a more detailed, longer prompt can cause MORE clarifying questions, not fewer. Verbosity is not the same as clarity. Specificity where it matters (output format) is what kills the modals.

**Practical rule:** if you want claude.ai to ship without asking, state your output format in one line. Example: *"OUTPUT FORMAT: Rendered SVG cartoon. No separate script."*

---

## What this pair does NOT show

- That the scaffold ("think step by step") causes clarifying questions. The long prompt doesn't contain the scaffold. You can't attribute its behavior to a line that isn't there.
- That the scaffold causes preamble bloat. Neither output had a visible preamble.
- That one version of the prompt is objectively better. The cartoon quality is effectively tied.

That question is being tested in parallel — round 2, both short prompts, explicit OUTPUT FORMAT line, scaffold line being the only diff. That's the clean test.

---

## Practical takeaway for your AlignAI Prompt Hub

The long prompt (`social_influenza_prompt_2026-04-18.md`) is a perfectly good brief for an illustrator or a multi-format handoff. Its "flaw" is that it mentions too many possible output formats, which makes chat UI stop and ask.

The short prompt is the one that ships without asking. If you want a reusable chat-UI-friendly prompt, the short version is closer to the target shape. Add one `OUTPUT FORMAT:` line and it becomes deterministic.

---

## Sources

- Long prompt run output: `/social/social_influenza_five_panel_psa.svg` + AskUserQuestion modal screenshots
- Short prompt run output: `/social/real_run_prompt2_output.md`
- Original long prompt: `/social/social_influenza_prompt_2026-04-18.md`
- Round 2 clean A/B: pending your re-run in two fresh chats with the prompts from today's round 2 message
