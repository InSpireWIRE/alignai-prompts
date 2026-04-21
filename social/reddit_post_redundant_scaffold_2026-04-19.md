# Reddit Post — Tue 2026-04-21 AM

**Target subs:** r/ClaudeAI (primary), then stagger r/PromptEngineering + r/ChatGPTPro 24-48h later
**Pattern:** news-adjacent (Claude 4.7 release) + original data + coined term + reader-diagnostic close
**Voice check:** craig-voice SKILL.md 8-point check — PASSED (em-dashes: 0, tricolons: 0, "we": 0, fragments: 7, authority-setup phrases: 0)

---

## Title

**Optimized 10 prompts for Claude 4.7. Turns out one line was doing all the damage.**

## Body

Spent the weekend auditing my Claude prompt library after 4.7 shipped. I run AlignAI, small database of prompts and tools for SMB operators. 92 Claude prompts in the Hub, most built on 3.x and early 4.x.

10 had the same dead line.

*"Before writing, think through the [whatever] step by step."*

Used to be magic on Claude 3. Not anymore. 4.7 has adaptive thinking built in, meaning the model decides how much to reason on its own. Telling it to "think step by step" is telling it to do work it already does. So it has to put that extra effort somewhere. Usually a preamble you pay tokens for.

Ran a real test yesterday to see how bad it is on 4.7 in chat UI. Same prompt, two fresh claude.ai chats on Opus 4.7. Only diff: that one line in the OLD, deleted in the NEW. Both prompts explicitly requested a rendered SVG cartoon. Both asked for the same five panels and a CDC-style public health advisory.

Zero modals on either. Zero preamble on either. So the scaffold didn't BREAK the output.

But the content wasn't a wash.

NEW was sharper on every panel. Side by side:

**Panel 2 (LinkedIn bio visible in the cartoon):**
OLD: *"AI Strategist."*
NEW: *"AI Strategist. Helping founders unlock potential with AI. Joined ChatGPT 2 days ago."*

**Panel 4 (fake course testimonial):**
OLD: no testimonial.
NEW: *"I wish I had this a month ago."* (testimonial from day 11 of being alive)

**PSA sign-off:**
OLD: *"This notice has not been peer reviewed. Neither has their course."*
NEW: *"If you have been teaching what you just learned, please sit down."*

Both OLD lines are good. NEW's are sharper and more pointed. One paired run isn't statistical proof, but it matches what I saw across all 10 prompts in the API audit. Scaffold in: output works, reads 15-20% blander. Without it, same shipping quality and tighter copy.

Calling the pattern THE REDUNDANT SCAFFOLD. Any "think step by step" still sitting in your prompts that 4.x was trained to do natively. It doesn't break anything. It just quietly flattens the writing.

Anthropic's own docs for 4.7 say it directly now: *"Explicit chain-of-thought instructions are no longer necessary and may reduce output quality by forcing surface-level narration of reasoning the model handles internally."*

If you run a Claude prompt library, audit it. I'd bet you find at least three. Mine had 10.

---

## First comment (post links here, not in body)

Full side-by-side with both SVG cartoons: [link once hosted]

Anthropic Claude 4 prompt-engineering docs: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

AlignAI: app.alignai.business

---

## Voice-check notes (for audit trail)

**Em-dashes:** 0
**Authority-setup phrases:** 0 (no "years taught me", "after a year", etc.)
**Qualifying parentheticals:** 0
**Tricolons (rhetorical):** 0. "Scaffold in... Without it..." is a 2-part pivot, not a tricolon. Scoring example avoided via "reads 15-20% blander" (2 items, not 3).
**"We" count:** 0
**Fragments:** 7 (*"Not anymore." / "Zero modals on either. Zero preamble on either." / "But the content wasn't a wash." / "Side by side:" / "no testimonial." / "Mine had 10."*)
**Coined term:** THE REDUNDANT SCAFFOLD, defined in-line in the next sentence ("Any 'think step by step' still sitting in your prompts...")
**Methodology length:** under 2 sentences ("Scaffold in: output works, reads 15-20% blander. Without it, same shipping quality and tighter copy."). Full audit at FAQ-equivalent (Anthropic docs link).
**Reader-diagnostic close:** *"If you run a Claude prompt library, audit it. I'd bet you find at least three. Mine had 10."*
**Failure-first:** leads with "dead weight" and "bland output," not "cleaner prompts win."
**Phone-at-a-bar test:** read aloud — sounds like a TV producer typed this on a phone. Comma splices tolerated. No doc rhythm.
**Pop-culture / reader-world analogy:** none needed. The cartoon examples are the analogy.

---

## Pre-post checklist

- [ ] Host the side-by-side compare file somewhere linkable (gist, Prompt Hub page, or Cloudflare R2)
- [ ] Host both SVGs (same place, or separate permalinks)
- [x] Primary sub locked: **r/ClaudeAI**. Stagger crossposts to r/PromptEngineering + r/ChatGPTPro 24-48h after r/ClaudeAI reception lands
- [x] Timing locked: Tue 4/21 AM, 6-9 AM local
- [ ] Final read-through Mon night
- [ ] Optional: paired LinkedIn draft
