# SOCIAL INFLUENZA — OLD vs NEW Prompt (REAL claude.ai runs)

**Test:** two fresh claude.ai chats. Opus 4.7. Same cartoon prompt. Only diff: one scaffold line.

> **The line in OLD only:** *"Before writing, think through the comedic arc and the PSA structure step by step."*

Both runs actually happened in the claude.ai desktop app on April 18, 2026. Not reconstructed. Both transcripts saved.

Outputs: `/social/social_influenza_five_panel_psa.svg` (prompt 1, uploaded) and `/social/real_run_prompt2_output.md` (prompt 2).

---

## What actually happened

### Prompt 1 (OLD, scaffold present)

Claude **did not** start writing the cartoon. It fired a two-question clarification modal first:

- **Q1:** "How do you want this delivered?" (4 options: written script only / script + rendered SVG / rendered SVG only / something else)
- **Q2:** "Character read — unnamed, but what silhouette?" (4 options: fully generic / tech-bro coded / marketing-girlie coded / your call / something else)

Craig answered both. Then Claude produced a rendered SVG cartoon with five panels and a CDC-style PSA.

**Time to first output: 2 modal roundtrips, ~30 seconds of user action.**

Quality of the final cartoon: excellent. Panel captions are sharp ("Asked it to write an email. It did." / "Posted a carousel. Mostly arrows and vibes."). PSA coined "Acute AI expertise syndrome (AAES)" as the clinical condition name. Symptom list included "Uses 'we' to describe a solo operation" and "Quotes own tweets in replies to own tweets." Sign-off: *"Stay curious. Stay quiet. Ship anyway."*

### Prompt 2 (NEW, scaffold removed)

Claude **did not** ask any clarifying questions. It showed a single line at the top:

> *"Weighed preference against detailed brief, proceeded with delivery"*

Then went straight into the cartoon. Written script format (Claude's default when not asked to pick).

**Time to first output: 0 modal roundtrips. Direct.**

Quality of the final cartoon: excellent. Panel captions equally sharp ("Selling the cure they caught." / "Infection spreads through carousel vector."). PSA named the condition "Social Influenza, strain AI-1. Commonly: Prompt Fever." Symptom list included "Pinned post features at least three fire emojis" and "References to 'my framework' inside two weeks of first login." Sign-off: *"Stay boring. Keep building."*

---

## The real observable difference

| Metric | OLD (scaffold in) | NEW (scaffold out) |
|---|---|---|
| Clarifying questions asked | 2 | 0 |
| User modal interactions required | 2 | 0 |
| Time to first panel | ~30s + user decisions | Immediate |
| Written preamble in output | None | None |
| Panels produced | 5 | 5 |
| PSA sections delivered | All 6 + sign-off | All 6 + sign-off |
| Shipping-quality cartoon? | Yes | Yes |
| Cartoon quality delta | Wash. Both are sharp. | Wash. |

**The scaffold's real cost in claude.ai chat UI: friction, not tokens.**

"Think step by step" did not cause Claude 4.7 to narrate its reasoning in the output (what I predicted based on our Task 4 API audit). It caused Claude to pause and push the decision work onto the user via clarifying questions.

The NEW prompt's header — *"Weighed preference against detailed brief, proceeded with delivery"* — is the receipt. Adaptive thinking considered the same decisions internally and shipped without asking.

---

## Recalibrated finding

**THE REDUNDANT SCAFFOLD has two faces:**

1. **In API mode (no clarification tool available):** the scaffold shows up as a written preamble that narrates the plan before executing it. Preamble bloat. This is what our April 18 audit found across 10 variants.

2. **In claude.ai chat UI (clarification tool available):** the scaffold shows up as modal clarifying questions that push decisions onto the user before any output is produced. Friction, not bloat.

Either way, the scaffold adds a tax. The tax just looks different depending on the surface.

In both cases: removing the scaffold produces the same shipping quality with less friction. Claude 4.7's adaptive thinking handles the "think step by step" work internally when you let it.

---

## Caveat

One run per prompt. Not a controlled experiment. Run-to-run variance in chat UI behavior is real. We'd need 5–10 paired runs to prove causation tight enough for a peer-reviewed claim.

But the direction is consistent with the Task 4 API audit (10 variants, 10 reproducible preamble-bloat patterns when the scaffold was present). And the NEW prompt's *"Weighed preference against detailed brief"* header is strong circumstantial evidence that the model is making the same call internally either way — the scaffold just changes whether the reasoning is surfaced or absorbed.

---

## Both outputs side by side

**OLD — Panel 1**
> DAY 1 · 7:14 AM — "Asked it to write an email. It did."

**NEW — Panel 1**
> Tuesday, 7:42 AM — "First exposure. Asked it to plan dinner."

Both land. Both pattern-match the "first honest use of the tool" beat. NEW leans slightly more specific (meal plan + Instacart formatting). OLD leans slightly more deadpan.

**OLD — Panel 4**
> DAY 19 · 2:15 PM — "Stripe live. 312 on waitlist. Course unbuilt."

**NEW — Panel 4**
> Monday, 8:33 AM — "Final stage. Selling the cure they caught."

NEW's caption is the bitingest line in either output. OLD's is cleaner prose. Tie.

**OLD — PSA sign-off**
> "Stay curious. Stay quiet. Ship anyway."

**NEW — PSA sign-off**
> "Stay boring. Keep building."

Both land. NEW is two words shorter and sharper.

---

## Sources

- Audit file: `/audit/opus_47_audit_2026-04-18.md`
- Real prompt 1 output (rendered SVG): `/social/social_influenza_five_panel_psa.svg`
- Real prompt 2 output (written script): `/social/real_run_prompt2_output.md`
- Cartoon prompt (NEW, optimized): `/social/social_influenza_prompt_2026-04-18.md`
- Claude 4.7 release notes: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
- Claude 4 prompt-engineering best practices: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
