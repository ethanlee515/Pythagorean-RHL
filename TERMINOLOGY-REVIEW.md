# Terminology review

Audience: cryptography/security and interactive theorem proving. Reviewed the
main manuscript, its appendices and figure text, and the alternative
introduction enabled by draft mode.

The terminology edits applied in this pass replace “law” according to its role:
required interface properties are **assumptions**, individual equalities are
**identities**, an inequality is a **bound**, and a random output has a
**distribution**. The output-distribution equation label was renamed as well.
The comment quoted from `ApproxFHE.v` was updated in both the parent artifact
and the manuscript's refreshed excerpt, preserving its source line numbers.
The mathematical statements and Rocq identifiers are unchanged.

The following are suggestions for review, not additional manuscript edits.
Some concern terminology specific to this paper or familiar to only one of
the two audiences; they are not all incorrect terms.

1. **“Local charts,” “metric charts,” and “isometry.”**
   See [introduction.tex](introduction.tex), line 158;
   [construction-security-setting-and-result.tex](construction-security-setting-and-result.tex),
   line 63; and the displayed `ApproxFheMetric` interface in
   [appendix-formal-interface-excerpts.tex](appendix-formal-interface-excerpts.tex),
   line 37. The maps are defined on the whole message/vector spaces, and the
   decoding map may identify distinct vectors. A reader may infer local
   bijections or a distance-preserving map between arbitrary pairs from the
   geometric terminology; the displayed assumptions instead give a distance
   identity relative to the chosen center. Prefer **integer-coordinate
   interface**, **coordinate encoding**, and **displacement decoding** in prose.
   Retain formal identifiers such as `inverse_isometry` when quoting the artifact,
   with an explanation that decoding need not be a two-sided inverse.

2. **“Equal-variance” and “standard deviation” for the discrete Gaussian.**
   See [construction-security-setting-and-result.tex](construction-security-setting-and-result.tex),
   line 188; [program-logic-for-adaptive-games.tex](program-logic-for-adaptive-games.tex),
   line 218; and [appendix-formal-interface-excerpts.tex](appendix-formal-interface-excerpts.tex),
   line 69. Prefer **discrete Gaussians with a common width parameter** and
   **positive width parameter**. For the displayed mass function, the actual
   variance is not generally the parameter `sigma^2`; in fact it is strictly
   smaller for positive finite width. See Canonne, Kamath, and Steinke,
   [Proposition 21](https://proceedings.neurips.cc/paper_files/paper/2020/file/b53b3a3d6ab90ce0268229151c9bde11-Supplemental.pdf#page=22).
   Integer shifts do preserve variance, so “equal-variance” is true for the
   compared distributions, but it can obscure the parameterization. In the
   proof explanation, say that the common width and integer-shift invariance
   make the normalizers equal. This also affects both introductions, the
   mechanization section, and the probability appendix.

3. **“Support-level correctness,” “good-execution case,” and “good key-pair
   boundary.”**
   See [construction-security-setting-and-result.tex](construction-security-setting-and-result.tex),
   line 48; [introduction.tex](introduction.tex), line 184; and
   [ethics-considerations.tex](ethics-considerations.tex), line 7.
   Use **approximate correctness with probability one** consistently, explaining
   once that it holds for every output in the relevant support. “Approximate”
   describes the numerical error bound, while “with probability one” describes
   the absence of correctness failures. “Good-execution case” can sound as
   though the theorem already conditions on a defined good event; **case
   without correctness failures** is clearer. The abstract's unqualified
   “approximately correct” also leaves this distinction implicit.

4. **“Paid hop,” “paid arrow,” and “paid step.”**
   See [reduction-and-missing-link.tex](reduction-and-missing-link.tex), line 53;
   [verified-compiler-for-adaptive-oracle-programs.tex](verified-compiler-for-adaptive-oracle-programs.tex),
   line 204; and the alternative introduction and AI-workflow appendix.
   These are informal shorthand. Prefer **game hop with nonzero statistical
   loss**, then **statistical hop** where the meaning is clear. Distinguish
   the per-call **KL budget** from the final **statistical-distance bound**;
   “call-error tuples” in
   [appendix-additional-probability-details.tex](appendix-additional-probability-details.tex),
   line 72, would be clearer as **KL-budget tuples**.

5. **“Local-to-adaptive theorem,” “selected-call compiler,” and “same-package
   correctness.”**
   See [introduction.tex](introduction.tex), line 144, and
   [verified-compiler-for-adaptive-oracle-programs.tex](verified-compiler-for-adaptive-oracle-programs.tex),
   line 1. These are defined descriptive names, but they create several new
   labels for the reader. Prefer **adaptive oracle replacement theorem** for
   the main result. Introduce the compiler as a **trace-based program
   transformation that exposes oracle calls**. Explain “same-package
   correctness” as **semantic preservation when selected and remaining calls
   use the same implementation**. Keeping “compiler” after that explanation
   is reasonable.

6. **“Conditional-coordinate preservation.”**
   See the theorem title in
   [program-logic-for-adaptive-games.tex](program-logic-for-adaptive-games.tex),
   line 181, and the contributions paragraph in
   [introduction.tex](introduction.tex), line 296. The title does not identify
   what is preserved. Prefer **statistical-distance bound from conditional KL
   budgets** for the displayed final bound, and **conditional KL composition
   bound** for the intermediate chain-rule result. The attributed name
   “Pythagorean probability preservation” can remain.

7. **“Additive indistinguishability.”**
   See [related-work.tex](related-work.tex), line 12. Prefer **an explicit
   statistical-distance bound for a complete adaptive program**. This states
   the guarantee directly and avoids requiring readers to infer whether
   “indistinguishability” is statistical or computational. The paper's own
   **additive-error judgment** is clearly defined and can retain its name.

8. **“Trusted base,” “trusted semantic base,” and “theorem boundary.”**
   See [mechanization-and-trusted-base.tex](mechanization-and-trusted-base.tex),
   line 222; [appendix-formal-interface-excerpts.tex](appendix-formal-interface-excerpts.tex),
   line 281; and the alternative introduction. For ITP readers, distinguish
   the **logical trusted computing base and foundational axioms**, the
   **definitions that must represent the intended security model**, and the
   **scheme assumptions required by the theorem**. Proven library results are
   checked dependencies, rather than additional unchecked inference rules.
   “Theorem parameters and assumptions” is usually more concrete than
   “theorem boundary.”

Two smaller consistency points:

- Use **total mass one** as the common explanation for “full distribution,”
  “weight-one,” and “full-mass.” Reserve **full support** for positive mass at
  every point; it is a different property. “Lossless” is familiar in
  probabilistic program verification and is already explained in the paper.
- **Up-to-bad**, **footprint**, **linking**, **judgment**, **coupling**, and
  **pushforward** are established terms in the relevant communities. Keep
  them, adding a short gloss where the other audience may need it. In
  particular, explain the first up-to-bad reference as a game hop whose extra
  loss is bounded by the probability of a correctness failure.

One nearby semantic wording issue deserves attention independently of naming:
[program-logic-for-adaptive-games.tex](program-logic-for-adaptive-games.tex),
line 54, says a unary Hoare triple makes the postcondition hold “with
probability one.” The artifact's `hoareJudgment` requires it on the support of
the output subdistribution and permits aborts. **Every non-failing outcome
satisfies the postcondition** states that partial-correctness guarantee without
implying losslessness.
