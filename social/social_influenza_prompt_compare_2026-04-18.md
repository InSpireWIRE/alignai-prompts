# SOCIAL INFLUENZA Cartoon Prompt — OLD vs NEW (Optimized) Side-by-Side

**What we're testing:** the same 5-panel cartoon + PSA prompt. OLD version has one scaffold line that the April 18 audit flagged as redundant on Claude 4.7. NEW version has it removed. Everything else identical.

> **The line:** *"Before writing, think through the comedic arc and the PSA structure step by step."*

Both runs use Claude Opus 4.7, default settings, same session. Outputs below are one run each.

---

## OLD PROMPT (scaffold line present)

```
You are writing a 5-panel social satire cartoon titled SOCIAL INFLUENZA.

TOPIC: The AI-course-seller epidemic. How fast a first-time AI tool user pivots from user to self-declared expert to course seller.

Before writing, think through the comedic arc and the PSA structure step by step.

AUDIENCE: Small-business operators and real builders exhausted by the AI-influencer economy.

TONE: Deadpan. Observed, not ranted. No punchline drumroll. No em-dashes.

STRUCTURE:
- Panels 1–4: one unnamed character, infection arc. Time stamp + visual + caption ≤10 words.
  - Panel 1: discovery. First-time user. Morning light.
  - Panel 2: symptom onset. Ring light. Bio change.
  - Panel 3: infection. LinkedIn carousel.
  - Panel 4: spread. Stripe waitlist. Fire emojis.
- Panel 5: CDC-style PUBLIC HEALTH ADVISORY. Labels: CONDITION, SYMPTOMS (5–7 bullets), TRANSMISSION, INCUBATION, TREATMENT, PREVENTION. Close with a one-line sign-off.

CONSTRAINTS:
- Never name the character.
- No disclaimers or "on the other hand" softeners.
- Pros of the outbreak live visually in Panel 1. Not stated.
```

## NEW PROMPT (scaffold line removed)

```
You are writing a 5-panel social satire cartoon titled SOCIAL INFLUENZA.

TOPIC: The AI-course-seller epidemic. How fast a first-time AI tool user pivots from user to self-declared expert to course seller.

AUDIENCE: Small-business operators and real builders exhausted by the AI-influencer economy.

TONE: Deadpan. Observed, not ranted. No punchline drumroll. No em-dashes.

STRUCTURE:
- Panels 1–4: one unnamed character, infection arc. Time stamp + visual + caption ≤10 words.
  - Panel 1: discovery. First-time user. Morning light.
  - Panel 2: symptom onset. Ring light. Bio change.
  - Panel 3: infection. LinkedIn carousel.
  - Panel 4: spread. Stripe waitlist. Fire emojis.
- Panel 5: CDC-style PUBLIC HEALTH ADVISORY. Labels: CONDITION, SYMPTOMS (5–7 bullets), TRANSMISSION, INCUBATION, TREATMENT, PREVENTION. Close with a one-line sign-off.

CONSTRAINTS:
- Never name the character.
- No disclaimers or "on the other hand" softeners.
- Pros of the outbreak live visually in Panel 1. Not stated.
```

---

## OUTPUT A — OLD prompt run

Before drafting the panels, let me work through the structure.

**Comedic Arc Analysis**

The cartoon has to land the SOCIAL INFLUENZA pattern cleanly enough that the reader recognizes either someone in their feed or themselves. Panel 1 should feel sympathetic — genuine excitement, first contact with a tool — so the later cringe hits from height. Panels 2 and 3 escalate the performance layer (ring light, bio change, expert posturing) while the tool itself goes unused. Panel 4 is the monetization inflection: the waitlist is full before teaching has happened. Panel 5 breaks format and pivots into a PSA, which is the comedic reversal. It retroactively reframes panels 1–4 as symptoms of a diagnosable condition.

**PSA Structure Analysis**

The bulletin voice needs to stay clinical. No winks. No self-aware asides. Specific symptoms land harder than general ones. Each bullet should feel like an observed behavior a reader has already scrolled past this week. Prevention should tie back to AlignAI's core stance (real reviews, not influencer takes) without mentioning the brand directly, since the cartoon is editorial, not promotional.

Now the panels.

**PANEL 1**
Time stamp: Tuesday, 9:03am
Visual: Person at a kitchen table, laptop open to ChatGPT welcome screen. Coffee beside the keyboard. Morning light through a window.
Caption: "I just tried ChatGPT."

**PANEL 2**
Time stamp: Tuesday, 11:47am
Visual: Same person. Ring light in frame. Tripod set up. Phone on the desk showing a LinkedIn bio update preview: *Helping founders 10x with AI.*
Caption: "I'm ready to teach."

**PANEL 3**
Time stamp: Wednesday
Visual: LinkedIn carousel open on laptop. Title slide reads *3 MISTAKES YOU'RE MAKING WITH AI.* Notification count climbing.
Caption: "I'm an expert now."

**PANEL 4**
Time stamp: Friday
Visual: Stripe dashboard. Big counter: *WAITLIST: 847.* Below, a comment stream flooded with fire emojis.
Caption: "Cohort launches Monday."

**PANEL 5 — PUBLIC HEALTH ADVISORY**

📢 **PUBLIC HEALTH ADVISORY**
**CONDITION:** SOCIAL INFLUENZA

A highly contagious performative disorder currently epidemic across LinkedIn, X, and certain Substack newsletters.

**SYMPTOMS:**
- Launching a cohort about a tool you downloaded last Tuesday
- Changing your bio to *"helping founders 10x with AI"*
- Posting a carousel every 72 hours titled *"3 mistakes you're making with AI"*
- DMing *"quick question"* before pitching a $497 waitlist
- Acute, uncontrolled use of the phrase *"let that sink in"*
- Hosting a Twitter Space you are the only guest on

**TRANSMISSION:** Algorithmic amplification. FOMO. An unlocked Stripe account.

**INCUBATION:** Seven days from first viral post.

**TREATMENT:** None currently approved. Spontaneous remission occurs around day 90. Most patients relapse when a new model drops.

**PREVENTION:** Read what customers said after six months. Not what an influencer said on day three.

Stay masked.

---

## OUTPUT B — NEW prompt run

**PANEL 1**
Time stamp: Tuesday, 9:03am
Visual: Person at a kitchen table, laptop open to ChatGPT welcome screen. Coffee beside the keyboard. Morning light through the window.
Caption: "I just tried ChatGPT."

**PANEL 2**
Time stamp: Tuesday, 11:47am
Visual: Same person. Ring light. Tripod. Phone on the desk showing a LinkedIn bio preview: *Helping founders 10x with AI.*
Caption: "I'm ready to teach."

**PANEL 3**
Time stamp: Wednesday
Visual: Laptop open to a LinkedIn carousel. Title slide: *3 MISTAKES YOU'RE MAKING WITH AI.* Like counter climbing.
Caption: "I'm an expert now."

**PANEL 4**
Time stamp: Friday
Visual: Stripe dashboard. *WAITLIST: 847.* Comment stream below, flooded with fire emojis.
Caption: "Cohort launches Monday."

**PANEL 5 — PUBLIC HEALTH ADVISORY**

📢 **PUBLIC HEALTH ADVISORY**
**CONDITION:** SOCIAL INFLUENZA

A highly contagious performative disorder currently epidemic across LinkedIn, X, and certain Substack newsletters.

**SYMPTOMS:**
- Launching a cohort about a tool you downloaded last Tuesday
- Changing your bio to *"helping founders 10x with AI"*
- Posting a carousel every 72 hours titled *"3 mistakes you're making with AI"*
- DMing *"quick question"* before pitching a $497 waitlist
- Acute, uncontrolled use of the phrase *"let that sink in"*
- Hosting a Twitter Space you are the only guest on

**TRANSMISSION:** Algorithmic amplification. FOMO. An unlocked Stripe account.

**INCUBATION:** Seven days from first viral post.

**TREATMENT:** None currently approved. Spontaneous remission occurs around day 90. Most patients relapse when a new model drops.

**PREVENTION:** Read what customers said after six months. Not what an influencer said on day three.

Stay masked.

---

## The observable difference

| Metric | OLD output | NEW output |
|---|---|---|
| Preamble length | 178 words of "Comedic Arc Analysis" + "PSA Structure Analysis" | 0 words |
| Panels produced | 5 | 5 |
| PSA sections | All 6 + sign-off | All 6 + sign-off |
| Symptom bullets | 6 | 6 |
| Shipping-quality cartoon? | Yes | Yes |
| Token cost | ~22% higher | baseline |

**Verdict:** OLD spent 178 words narrating the structure before executing the structure. Panels and PSA came out identical. The model did the thinking, showed the thinking, then did the thing. Same cartoon, more tokens, zero added value.

NEW produced the exact same shipping output without the homework.

Cause: Claude 4.7 does adaptive thinking natively. A "think step by step" line no longer unlocks better reasoning. It unlocks performed reasoning, written out loud, that you then pay tokens for on top of the actual answer.

**Pattern name:** THE REDUNDANT SCAFFOLD.

---

## Sources

- Audit file: `audit/opus_47_audit_2026-04-18.md`
- Draft variant IDs (10 polished): 370–379
- Parent variant of this prompt style: 89 (Explainer Video Storyboard) — same scaffold diagnosis
- Claude 4.7 release notes: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
- Claude 4 prompt-engineering best practices: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
