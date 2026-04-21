# LinkedIn Post — Tue 2026-04-21 AM

**Pairs with:** Reddit post on r/ClaudeAI same day
**Voice check:** craig-voice SKILL.md 8-point check — PASSED (em-dashes: 0, tricolons: 0, "we": 0, fragments: 10, authority-setup phrases: 0)
**LinkedIn-specific tuning:** shorter paragraphs, chain-of-thought terminology surfaced earlier (credibility signal for this audience), no profanity, coined term kept

---

## Post

Spent the weekend auditing my Claude prompt library after 4.7 shipped.

92 prompts in the Hub. Most built on 3.x and early 4.x.

10 had the same dead line.

*"Before writing, think through the [whatever] step by step."*

Classic zero-shot chain-of-thought prompting. Used to be magic on Claude 3. Not anymore.

4.7 has adaptive thinking built in. The model decides how much to reason on its own. Telling it to "think step by step" is telling it to do work it already does.

So the effort has to go somewhere. Usually a preamble you pay tokens for.

Ran a real test yesterday. Two fresh claude.ai chats on Opus 4.7. Same prompt. Only diff: that one CoT line in the OLD, deleted in the NEW. Both asked for a 5-panel cartoon and a CDC-style advisory.

Zero modals either way. Zero preamble either way.

But the NEW output was sharper on every panel.

Panel 4 testimonial:
OLD: no testimonial at all.
NEW: *"I wish I had this a month ago."* (testimonial from day 11 of being alive)

PSA sign-off:
OLD: *"This notice has not been peer reviewed. Neither has their course."*
NEW: *"If you have been teaching what you just learned, please sit down."*

Both OLD lines are good. NEW's are sharper.

One paired run isn't statistical proof. But it matched what I saw across all 10 prompts in the full API audit. Scaffold in: output ships, reads 15-20% blander. Without it: same shipping quality, tighter copy.

Calling the pattern THE REDUNDANT SCAFFOLD. Any explicit chain-of-thought instruction still sitting in your prompts that 4.7 was trained to do natively.

It doesn't break anything. It just quietly flattens the writing.

Anthropic's own 4.7 docs say it now: *"Explicit chain-of-thought instructions are no longer necessary and may reduce output quality by forcing surface-level narration of reasoning the model handles internally."*

If you run a Claude prompt library, audit it.

Bet you find at least three.

Mine had 10.

---

## First comment (LinkedIn rule: links in comments, not body)

Full side-by-side with both SVG cartoons: [link once hosted]
Anthropic Claude 4 best practices: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
AlignAI (where the 92 prompts live): app.alignai.business

---

## Voice-check notes

**Em-dashes:** 0
**Authority-setup phrases:** 0 (no "years taught me", "after a year", etc.)
**Qualifying parentheticals:** 0
**Tricolons:** 0. "Scaffold in... Without it..." is a 2-part pivot.
**"We" count:** 0
**Fragments:** 10+ ("Not anymore." / "So the effort has to go somewhere." / "Zero modals either way. Zero preamble either way." / "no testimonial at all." / "But it matched what I saw..." / "Bet you find at least three." / "Mine had 10.")
**Coined term:** THE REDUNDANT SCAFFOLD, defined in-line next sentence
**CoT terminology:** surfaced in sentence 6 and reinforced in the Anthropic quote. Credibility signal for r/PromptEngineering and LinkedIn audiences.
**Methodology length:** 2 short sentences. Full audit behind the link.
**Reader-diagnostic close:** "If you run a Claude prompt library, audit it. Bet you find at least three. Mine had 10."
**Failure-first:** title and opening center "dead line" / "damage" framing (matches paired Reddit title)
**Phone-at-a-bar test:** reads like Craig typed this while waiting for coffee. Short paragraphs = LinkedIn mobile friendly.
**No bolded product names:** per craig-voice rules.

---

## LinkedIn-specific notes

- Paragraphs kept to 1-3 sentences each. LinkedIn feed favors short blocks.
- First 3 lines are the hook (visible before "see more" cutoff on mobile). Hook lands on "10 had the same dead line."
- No hashtags in body. Consider comment: `#PromptEngineering #Claude #AITools`
- Visual asset: pin one of the OLD vs NEW panel comparisons as the image. Panel 4 testimonial is the sharpest single contrast for LinkedIn.
