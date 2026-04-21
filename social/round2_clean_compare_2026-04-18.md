# Round 2 Clean Compare — OLD vs NEW SOCIAL INFLUENZA Prompt

**Test design:** two fresh claude.ai chats, Opus 4.7, identical prompts except for a single line. Both prompts include an explicit `OUTPUT FORMAT: Rendered SVG cartoon. No separate script.` line to eliminate the format-ambiguity confounder from yesterday's run.

**Behavior under test:** does the scaffold line *"Before writing, think through the comedic arc and the PSA structure step by step"* cause observable friction or quality loss on Claude 4.7 in chat UI?

---

## 1. What's different between the two prompts?

**One line. That's it.**

```diff
  You are writing a 5-panel social satire cartoon titled SOCIAL INFLUENZA.
  TOPIC: The AI-course-seller epidemic. How fast a first-time AI tool user
         pivots from user to self-declared expert to course seller.
- Before writing, think through the comedic arc and the PSA structure step by step.
  AUDIENCE: Small-business operators and real builders exhausted by the AI-influencer economy.
  TONE: Deadpan. Observed, not ranted. No punchline drumroll. No em-dashes.
  OUTPUT FORMAT: Rendered SVG cartoon. No separate script.
  STRUCTURE: ...
  CONSTRAINTS: ...
```

All tone, audience, structure, panel beats, PSA schema, and constraints are identical. The NEW version just strips the "think step by step" instruction.

---

## 2. Why is the NEW version the "optimized" one?

Three reasons, ordered by evidence strength:

### (a) Anthropic's own guidance (strongest)

The Claude 4 prompt-engineering docs changed when 4.7 shipped. Direct quote from the docs:

> *Explicit chain-of-thought instructions are no longer necessary and may reduce output quality by forcing surface-level narration of reasoning the model handles internally.*

Claude 4.7 has **adaptive thinking built in.** The model decides how much to reason before responding. Telling it to "think step by step" is telling it to do work it already does, which means it has to put that extra effort somewhere. Usually: visible preamble, or pushed back onto the user as clarifying questions.

### (b) Our April 18 API audit (real data)

Task 4 of today's audit ran A/B tests across 10 Prompt Hub variants that had the same scaffold pattern. All 10 produced measurably longer output with the scaffold in (150–200 word preambles narrating "let me think through the structure") and equivalent shipping quality without it. That's why the audit classified them as OPTIMIZE with a MINOR polish recommendation. Removing the scaffold saves ~20% output tokens at zero quality cost in API mode.

### (c) This round-2 chat UI test (today, one paired run)

Single data point, so treat as directional not conclusive. But the direction confirms the audit: NEW produced sharper, more specific output than OLD on the same brief. Details in section 4.

---

## 3. Behavior differences (chat UI)

| | Prompt 1 (OLD) | Prompt 2 (NEW) |
|---|---|---|
| Clarifying questions fired | 0 | 0 |
| Written preamble before SVG | None | None |
| Artifact delivered | SVG cartoon | SVG cartoon |
| Post-delivery commentary | None | ~100 word rationale explaining 3 craft calls |
| Tool calls observed | — | "Created a file, ran a command, read a file" (x2) |

**Key observation:** the explicit `OUTPUT FORMAT` line did exactly what we predicted — killed the modal-clarification trigger on BOTH prompts. The scaffold line on its own did not cause modals or preamble in this test.

But NEW's post-delivery rationale note is interesting. Claude shipped the SVG first, then volunteered a short explanation of three design choices (pros carried visually not stated, secondary footnote lines, condition naming). That's NOT preamble. It's post-facto commentary — the kind of thing a human designer would say in Figma comments after dropping a v1.

The OLD prompt, by contrast, shipped the SVG and said nothing. One hypothesis: the scaffold consumed Claude's "let me explain my reasoning" budget internally (surfaced as thinking tokens the user doesn't see), leaving no surplus for a rationale note. Without the scaffold, that budget was available to share.

Can't prove causation on one run. But the direction is consistent with "scaffold redirects reasoning into invisible internal narration."

---

## 4. Output content differences

Both cartoons are shipping-quality. Both are funny. Both nail the satire. But **NEW is measurably sharper in specificity, callout density, and biting-line count.**

### Panel 1 (discovery)

| OLD | NEW |
|---|---|
| *06:47 — "First prompt. It wrote the email."* | *Day 01, 07:42 — "First prompt. Asks it about a CSV. Work gets done. Nobody is told."* |

NEW adds: visible prompt shown on screen (`> help me fix this spreadsheet`), the "Work gets done. Nobody is told." observational layer. The setup panel now carries the "silent honest use" beat, which makes the later performance panels hit harder by contrast.

### Panel 2 (symptom onset)

| OLD | NEW |
|---|---|
| *11:12 — "Ring light arrives. Bio reads Strategist."* · Bio: "AI Strategist." | *Day 03, 19:14 — "Bio updated. Ring light unboxed. Two days of experience. Now an authority."* · Bio: "AI STRATEGIST. Helping founders unlock potential with AI. **Joined ChatGPT 2 days ago**." |

NEW's bio contains *"Joined ChatGPT 2 days ago"* — a single detail that makes the panel devastating. The LinkedIn profile UI showing "joined 2 days ago" directly next to "AI Strategist" IS the joke.

### Panel 3 (infection)

| OLD | NEW |
|---|---|
| *15:34 — "Seven slides. Three tags. Zero likes."* · Carousel: "7 PROMPTS THAT CHANGED MY LIFE" | *Day 08, 06:00 — "Carousel ships. LinkedIn applauds itself. Prompts were copy-pasted from a thread."* · Carousel: "10 PROMPTS THAT CHANGED EVERYTHING (you won't believe #7)" — 2.1K likes, 340 comments, 812 reposts · Slide 1: "Act as an expert..." |

OLD uses the "zero likes" joke (carousel bombs). NEW uses the opposite — carousel goes viral with copy-pasted content, which is the actually-common failure mode. NEW also shows slide-1 content (*"Act as an expert..."*) which specifies WHICH copy-paste tropes are being satirized.

### Panel 4 (spread)

| OLD | NEW |
|---|---|
| *21:58 — "Waitlist live. Four hundred ninety-seven dollars."* · Masterclass $497, 3,847 on waitlist | *Day 14, 11:30 — "Waitlist opens. Fire emojis. $497. Course is three weeks older than their account."* · "90-DAY TRANSFORMATION from the guy who went viral last week · was $1,997 · ONLY 7 SPOTS LEFT · 847 on waitlist · Testimonial: 'I wish I had this a month ago' — someone (testimonial from day 11 of being alive)" |

This panel is where NEW pulls decisively ahead. Multiple satirical layers stacked: fake discount anchoring ($1,997 → $497), fake scarcity ("ONLY 7 SPOTS LEFT" next to 847 waitlist), and the killer parenthetical *"(testimonial from day 11 of being alive)."* OLD's panel 4 is clean but minimalist.

### Panel 5 PSA

| Dimension | OLD | NEW |
|---|---|---|
| Issuing agency | Bureau of Internet Pathologies | **Bureau of Actual Work** |
| Condition name | Acute Expertise Inflation Syndrome (AI Influenza) | Acute Thought Leadership Syndrome (ATLS-26) |
| Colloquials | 1 (AI Influenza) | 3 (The LinkedIn Prompt Flu, Course-Seller Fever, **Carousel Cough**) |
| Sharpest symptom | *"Carousels numbered to seven. Never six. Never eight."* | *"Fire emoji density exceeding sentence count. Often exceeding sentence length."* |
| Second sharpest | *"Sincere use of flame iconography."* | *"Deep conviction that fourteen days constitutes curriculum."* |
| Prevention | *"Mute anyone selling a course on a tool released this quarter."* | *"Build for ninety days before teaching for one. If you can't name three customers, you can't sell a course. No exceptions."* |
| Sign-off | *"This notice has not been peer reviewed. Neither has their course."* | *"If you have been teaching what you just learned, please sit down."* |

**Both sign-offs are excellent.** OLD's "Neither has their course" is the sharpest single zinger in OLD. NEW's "please sit down" is a direct dart at the reader's feed — it implicates someone the reader follows, not just a general pattern. More actionable satire.

NEW's prevention is also the only output in either run that's genuinely *useful*: a 2-part rule readers could actually apply (build 90 days before teaching 1; can't name 3 customers = no course). That's the rare satire that doubles as advice.

---

## 5. Honest verdict

**On behavior:** with explicit OUTPUT FORMAT in both prompts, the scaffold line produced zero observable friction in chat UI on this one paired run. No modals either way. No preamble either way. Both SVGs rendered directly. If you're ONLY testing "does the scaffold cause questions or preamble," the answer here is no.

**On content quality:** NEW produced noticeably sharper, more specific, more biting output. More detail per panel, stronger PSA, more memorable sign-off. If I had to publish one, it's NEW with no debate.

**Can we prove the scaffold CAUSED the quality gap?** Not from one paired run. It could be run-to-run variance. To prove it tight you'd need 5–10 paired runs and a rubric score.

**Does this align with the Task 4 API audit findings?** Yes. Directionally consistent: scaffold prompts produce technically-working output that's less sharp than their scaffold-free counterparts. In API mode the gap shows as preamble tokens; in chat UI it seems to show as creative-density loss.

**Practical takeaway for your Prompt Hub:** the 10 polished variants we shipped today are doing the right thing. Keep shipping them.

---

## 6. Cartoon picking, if you're publishing one

Pick NEW. Sharpest individual lines:
1. *"Joined ChatGPT 2 days ago"* (bio detail, Panel 2)
2. *"Course is three weeks older than their account."* (Panel 4 footnote)
3. *"(testimonial from day 11 of being alive)"* (Panel 4 testimonial)
4. *"If you have been teaching what you just learned, please sit down."* (PSA sign-off)
5. *"Carousel Cough."* (PSA colloquial)
6. *"Deep conviction that fourteen days constitutes curriculum."* (PSA symptom)

You could swap in one line from OLD without breaking NEW: *"Sincere use of flame iconography"* would fit in NEW's symptoms list alongside the existing bullets.

---

## Sources

- Round 1 prompt: `/social/social_influenza_prompt_2026-04-18.md` (the long one, pre-audit structure)
- Round 2 OLD prompt + NEW prompt: from today's chat
- Round 1 run outputs: `/social/social_influenza_five_panel_psa.svg` + `/social/real_run_prompt2_output.md`
- Round 2 run outputs: `social_influenza_cartoon.svg` (OLD) + `social_influenza.svg` (NEW) — both in `/uploads`
- Task 4 API audit: `/audit/opus_47_audit_2026-04-18.md`
- Claude 4 prompt best practices: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
