# Appendix F rewrite

Our formalization is heavily AI assisted.
In this appendix, we answer the question from the other direction:
what is the *human* effort involved in producing our formalization.
We note that this section is for historical interest, of working with AI agents through mostly summer 2026.
As AI agents improve very quickly, it is expected that a state-of-the-art agent will be able to do this more independently and cheaply.

We split our discussion roughly as the main sections: real analysis and probability analysis, program logic soundness, compiler construction, and CKKS.
In each section, we proceed chronologically as much as we can.
Finally, we note the efforts on the AI part.

## Evidence added for the November 8 rewrite

The new LaTeX follows the structure below. Detailed provenance, the exact
episode selections, and a map to material retained outside the paper are in
[AI-ASSISTANCE-REWRITE-NOTES.md](AI-ASSISTANCE-REWRITE-NOTES.md). The existing
[audit notes](AI-ASSISTANCE-NOTES.md) and frozen exports retain the longer
usage/rework account. The original brainstorming bullets below are preserved.

Count requests and completed agent turns separately. Automatic goal
continuations can produce agent turns without new human instructions;
requests also include retries and routine directions. None of these counts
measures researcher hours. The following are selected episodes, with
overlapping scientific responsibilities, rather than complete per-layer totals.
Conversation dates use UTC.

| Part | Established dates and interaction counts | Human work to emphasize |
| --- | --- | --- |
| Analysis | Gaussian KL work entered May 6; preservation target May 16; final June 19–21 analysis/assumption push: 60 requests, 82 completed turns; June 22 Gaussian-rule restoration: 8 requests, 8 turns | Questioning totalized nonconvergent sums; making KL finiteness explicit; asking for LaTeX proofs of summability, the chain bound, and Pinsker; directing proof organization. Earlier conversations are missing, so no total round-trip count is available. |
| Logic | Initial Rocq encodings July 12–14, 2025; proposed rule/soundness statements July 14; hidden-mixture repair June 7, 2026; initial sequence proof June 9–11: 51 requests, 50 turns; missing-mass review/completion June 12–13: 28 requests, 28 turns | The early statements were prototypes, not completed soundness proofs. Preserve the shared intermediate value as a zero-budget coordinate; use completion for missing subdistribution mass. Include the May 31 counter-budget detour that human questioning did not immediately resolve. |
| Compiler | Human request for adaptive factoring May 31; selected construction/correctness work June 3–6: 47 requests, 45 turns; quantitative analysis continued through June 21 | Human specification and partial scaffold, already AI-assisted; correction of unnecessary bounded-call premise for semantic preservation; June 6 construction redesign and proof repair. |
| Noise flooding | Existing 2025 scheme/game interfaces and August 11 target; extended proof tasks from June 30; through the July 10 milestone: 46 requests, 297 completed turns, 269 automatic continuations | Human security objective and proof outline; July 9 chart-assumption objection and shared-postprocessing repair; **July 11 adversary-dependent security-bound correction**, after the first milestone; explicit reduction and H0–H6 presentation. The checked application is abstract approximate HE, with concrete CKKS instantiation external. |
| Cleanup | July 13: 3,933 application, 1,888 logic, and 1,634 probability lines deleted; 7,335 net reduction | Prune unused routes, but retain the Gaussian tail theorem for future imperfect-correctness work. Deleted code is not a measure of wasted AI effort. |
| Usage | Formalization: 3,347.688M tokens, 110.76 reported agent hours, US$2,231.82 API equivalent; full extended sample: 3,686.615M tokens, 124.40 hours, US$2,476.66 | Keep one purpose-allocation table in the appendix. Actual subscription cost and total human labor are not reconstructed. The frozen November 4 audit excludes this rewrite. |

The original model-specific US$200 reconstruction conjecture is retained in
the rewrite notes, with its untested status, rather than leading the paper's
historical narrative. The records also cannot tell us whether each skeptical
human checkpoint saved or cost time relative to independent agent work.

## Original subsection prompts

## Real and Probability Analysis

In this subsection, we recall our efforts towards proving lemma D.3.
That is, Pythagorean preservation, for MathComp distributions.
The other challenge is to prove the KL divergence between two discrete Gaussians.

* We started on the week of DD/MM, and took ~X days, using a total of ~Y round-trips (turns) with the AI agent.
  (The number of chats is probably less of a good metric.)
* (Was there any roadblocks? Or just a deep real-analysis hole that we had to spend days to fill?)
* Maybe say the human programmer was skeptical here and kept asking for LaTeX of what the agent was gonna formalize. If we had better hindsight now, we could also say if we saved the agent any time at all or if we just wasted money/time.

## Program Logic Soundness

In this subsection, we recall our efforts towards showing our program logic is sound.

* We started with PDF version which ended up needing some soundness fix
* We wrote down the judgments in Rocq on MM/DD, and formalized a soundness rule on MM/DD.
* In June (which day?), along the way towards proving soundness, we found bug #1 about hidden mixtures.
* In MM/DD, we found bug #2 about "completing" distributions (?)
* In MM/DD, after ?? turns, we proved the ?? rule. We then deleted X lines of code unused along the way.

## Compiler

* The idea of using a compiler was human.
* The rest of the story in Appendix F is fine I think...
* Maybe add how many turns this took

## CKKS

* Maybe the story currently in Section F.D is fine too?
* Also say how many turns this took
* The story of finding a bug with the chart assumptions probably go here too.

## AI costs

* This costs X tokens, Y hours of AI runtime.
* This is $Z in usage, if one were to buy the API directly.
