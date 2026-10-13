# Evidence for the AI-assistance appendix

Working notes for the authors; this file is not an input to the manuscript or
its source-package script. The appendix is in
`acknowledgment-of-ai-assistance.tex` and is included after the technical
appendices in both manuscript formats.

The account combines the author's recollection supplied on October 13, 2026,
the local Git histories, and retained Codex conversations. The relevant local
conversations located for this reconstruction begin on May 29, 2026. Earlier
AI assistance is recorded in Git, but the available conversations do not
establish its full extent. Git coauthor footers establish recorded assistance,
not a percentage of authorship; their absence does not establish that work was
entirely manual. Dates below follow the commit's recorded date or, for
conversations, its UTC timestamp.

## Chronology and supporting records

| Episode | Evidence | What it supports |
| --- | --- | --- |
| Initial logic encodings, July 2025 | Artifact commits `6e14495`, `d40b2ff`, `c2834de` | Judgments and initial inference rules existed well before the intensive 2026 proof work. Their manual origin and the preceding LaTeX design are the author's recollection. |
| FHE interfaces and games, July–August 2025 | Artifact commits `6abc881`, `67e8fe1`, `766ce5c`, `34b7e9d` | Early correctness, IND-CPA, IND-CPAD, and security-target statements. `34b7e9d` explicitly contains an admitted theorem and placeholder noise/security parameters; the final quantitative statement was not already complete. |
| Early manuscript | Manuscript initial import `257a030`, September 2025 | LaTeX judgments, proposed rules, a soundness subsection, and the intended square-root composition argument existed in the early draft. The import date does not date the original writing. |
| Return to AI-assisted proofs, May 2026 | Artifact commits `6ed6bf7`, `f68ae73`, `b8eb9ff`, `539a2c5`, `3183b79`, `2ba4a9c` | Work resumed in May, rather than only in summer. Some probability work records both Codex and Copilot assistance; proposed sequence rules required soundness repairs. |
| Nominal migration, May 28–29 | Artifact commits `bdb3b68`, `85a8e2f`, `2d388f4` | Adoption of the nominal extension preceded the trace compiler and involved Codex-assisted interface repairs. |
| Need for adaptive factoring, May 31 | Session `019e7d58-95c7-7060-8ff9-3e61eca1eacc`, initial user message | The author already identified the query-counting problem and asked about compiling general adversaries into factored ones. |
| Trace/replay construction, June 3–4 | Artifact commits `c167990`, `e7609e2`, `7460a2b`; sessions `019e8fb1-2e3b-7231-809b-fa5fdc8551ca` and `019e90a7-f2a7-7531-aa0b-ee209620261d` | The author supplied a partial implementation for review, including new suspension/traversal scaffolding, and Codex implemented its TODO. The earlier trace/replay commit also records Codex assistance, so the entire skeleton should not be attributed exclusively to the author. The author challenged an unnecessary bounded-call premise and noticed that residual calls require linking. |
| Compiler correctness, June 4 | Session `019e90bf-05a3-7380-ad22-2133fb7d5005`; artifact commits `83bb12b`, `6f796d0`, `501ea2c` | An explicit author request to prove correctness or break it into lemmas, followed by Codex-assisted proof work. The first proof was subsequently repaired and the construction revised. |
| Zero-budget coordinates, June 7 | Session `019e9fbc-8458-7c13-8389-403a7a23eba0`, especially messages at 02:10, 02:11, 02:35, and 02:53 UTC; artifact commit `162cc37` | The author questioned mixture preservation; Codex provided a hidden-mixture counterexample; the discussion retained a zero-budget branch coordinate. The author also questioned whether dropping it would be sound. These coordinates address conditioning, beyond simplifying proofs. |
| Missing mass and completion, June 12–13 | Sessions `019ebce8-0a3b-7593-9573-7fd944a290ec` and `019ebeb6-6c18-7300-b084-bcd7a98117a1`; artifact commits `b81d93b`, `4242f48`, `6a30c03`, `a53cf79` | The author identified a false full-mass implication, asked about null programs, and proposed reusing completion. The completed judgment, sequencing proof, and conversion rule were developed interactively. |
| Extended proof tasks, June 20–21 | Sessions `019ee3d0-38d7-7e00-a640-e18d807764ad` and `019ee58d-e712-70b1-92d4-3c3f5974ea83`; artifact commit `9799d05` | Delegation of extended assumption-discharge work, including compiler and Pinsker analysis, with author checkpoints and preference for a top-down proof. |
| Application proof, June 30–July | Sessions `019f1816-c139-7d12-8c0a-1108b4687a5f`, `019f1edf-fab7-72b0-9ea7-7373d8b16719`, and `019f4224-099b-7d53-879f-23e05ef54fd2` | Explicit persistent-goal requests to prove the noise-flooding result from the existing outline and compiler rule, with progress records and intervening review. |
| Chart-assumption correction, July 9–10 | Session `019f4224-099b-7d53-879f-23e05ef54fd2`, July 9 at 15:27 and 15:44 UTC; artifact commits `5021745`, `e526e7f`, `da878fb` | The author challenged `finite_common_inverse_isometry_encoding` and proposed sample-then-postprocess reasoning. The subsequent proof used origin-centered chart translation and removed the problematic proof route. |
| H0–H6 presentation, July 10 | Same session, user messages at 11:06, 12:24, 12:39, 12:45, and **12:50:36 UTC**, then Codex responses at 12:50–12:51; manuscript commit `54a48db` | Codex drafted and explained the detailed chain, but the author explicitly proposed the seven-stage organization, adding original and linked games before the compiled representation. It was not entirely an AI-originated presentation. |
| Conceptual games versus implementation stages, late July | Session `019f9f4e-754f-78c0-8780-badace3928e5`; manuscript commit `7d7df47` | Further author feedback questioned treating all seven stages as cryptographic hybrids, leading to the distinction retained in the current draft. |
| Broader manuscript revisions | Manuscript commits `9e23aef`, `53558da`, `9f91a0c` and the associated July–August sessions | Extensive Codex drafting, restructuring, and repeated author feedback; the existing acknowledgment was retained rather than removed. |

Recorded session metadata identifies `gpt-5.5` for the inspected May–July
proof sessions, `gpt-5.6-sol` for subsequent manuscript sessions, and
`gpt-6.1-sol` for the inspected October revisions. Some smaller editorial
sessions used other models. These identifiers describe major observed phases,
not every model or every interaction, and are retained here rather than in the
manuscript's opening historical note.

The October 13 revision adds the author's conjecture that an independent
GPT-6 Astra agent could reconstruct the full formalization from the manuscript
with Rocq excerpts removed, for at most US$200 in model usage. No reconstruction
experiment or cost measurement has been performed. A future experiment would
need to exclude access to the existing artifact, including through manuscript
links, while permitting the stated dependencies.
[Official GPT-6 Astra documentation](https://developers.openai.com/api/docs/models/gpt-6-astra),
checked on October 13, lists standard token rates of US$10 per million input
tokens and US$50 per million output tokens, with different rates for caching,
long contexts, and other processing modes. These rates do not establish the
total cost or feasibility of reconstructing this development. The appendix
therefore explicitly presents both the proposed outcome and budget as
conjectural.

The current trusted-base discussion is authoritative for the final
assumptions. This historical reconstruction does not perform a new Rocq
assumption audit and does not claim that the inherited MathComp summation
assumption has disappeared.
