# CSF 2027 readiness assessment

## Verdict

This project is a genuine CSF fit, not a fool's errand.  The venue explicitly
lists computer-aided cryptography and formal verification, and SSProve itself
is a CSF precedent.  The strongest defensible story is:

> A machine-checked good-execution IND-CPAD-to-IND-CPA reduction that preserves
> the parameter-critical square-root loss for adaptive decryption queries,
> powered by a reusable quantitative relational program logic and a verified
> local-to-adaptive oracle rule for SSProve.  Imperfect correctness is isolated
> as one standard up-to-bad transition.

The current artifact does **not** justify the stronger story that it fully
verifies the LMSS defense for CKKS.  Presenting it that way would invite a
well-founded rejection.

## Submission recommendation

The rewritten manuscript is suitable for serious internal review now.  The
conditional framework-and-case-study result is defensible at CSF if the paper
clearly distinguishes its checked good-execution theorem from the aggregate
correctness-failure bound required of an instantiation.  If the intended
headline is a verified concrete approximate-FHE defense, wait for a later CSF
cycle.

CSF 2027 has rolling deadlines on August 3 and October 15, 2026, and January
28, 2027.  The official call permits 12 pages of IEEE two-column main text,
excluding the AI-use acknowledgment, bibliography, and well-marked appendices:
[CSF 2027 call for papers](https://www.ieee-security.org/TC/CSF2027/cfp.html).

Given the current date, the October cycle leaves useful time for a chart
instantiation and an independent proof audit, but nonzero correctness is not by
itself a reason to abandon the submission: its proof extension is a standard
and cleanly isolated game hop.

## Review pressure points and extensions

1. **One-hop correctness extension — positioning resolved; mechanization
   optional.**  The abstract, theorem-boundary discussion, and conclusion now
   state the checked result as a good-execution theorem and give the
   <code>Pr[Bad_corr]</code> extension explicitly.  They also say what an
   instantiation must supply if that aggregate probability is derived from
   per-operation errors.  This is no longer a live manuscript problem.  A
   mechanized generic up-to-bad wrapper would be a useful strengthening, but it
   is not required for the current framework claim and would not provide the
   missing scheme-specific aggregate failure bound.

2. **Concrete chart instantiation — live; highest-value technical
   extension.**  Proving the origin-centered chart laws for at least one
   meaningful plaintext model, including wraparound and decoding, would
   materially strengthen relevance and auditability.  This is the main
   remaining research extension.  It is not a blocker if the paper is
   submitted as a program-logic/framework result with a conditional
   noise-flooding case study; it is a blocker for any headline claiming a
   verified concrete CKKS defense.

3. **Conventional PPT audit — resolved.**  The abstract, theorem-boundary
   discussion, theorem-boundary table, artifact audit, and conclusion all
   explain that SSProve places PPT in the metatheory and record the direct
   audit of this reduction.  No runtime semantics should be added for this
   submission.  A human author should merely confirm that the final explicit
   reduction still matches the stated audit after later edits.

4. **Inherited MathComp residue — resolved for submission; monitor only.**
   The TCB section now distinguishes the installed dependency graph from the
   locally proved mathematical obligation, reports the exact inherited name,
   records the <code>Qed</code> replacement and its
   <code>Print Assumptions</code> result, and avoids claiming that the current
   graph is literally axiom-free.  The proof is in
   [MathComp Analysis PR #2007](https://github.com/math-comp/analysis/pull/2007);
   as checked on July 24, 2026, the PR is open, cleanly mergeable, and assigned
   to the 1.17.0 milestone.  There is no remaining local mathematics to do and
   no benefit in carrying a private dependency fork solely to rename the
   inherited assumption.  If a suitable upstream release appears before the
   artifact freeze, pin it, rebuild, and refresh the assumption report.
   Otherwise retain the present disclosure.  Remove the PR URL and other
   author-identifying metadata from the double-blind artifact snapshot.

5. **Independent proof audit — live; pre-submission requirement.**  The
   development and manuscript are substantially AI-assisted.  A human author
   must inspect the specification hot path, run
   <code>Print Assumptions</code> on an explicit functor instantiation, and
   spot-check the compiler, conditional-KL/summability, discrete-Gaussian, and
   final game-bridge proofs.  A clean rebuild is necessary but does not replace
   this semantic audit.

In short, items 3 and 4 are closed, and item 1 is closed as a framing issue.
Items 2 and 5 remain genuinely live.  Of those, item 5 is a submission
requirement; item 2 is the strongest optional research enhancement.

## Packaging checklist

- Replace all repository links with an anonymized artifact snapshot.
- Scrub Git metadata, usernames, absolute paths, and generated-file metadata.
- Pin exact opam package versions; <code>rocq-ssprove</code> currently reports
  a development version rather than a release identifier.
- Add a one-command artifact check that builds the theorem and prints its
  assumptions.
- Have every author review the AI-use acknowledgment against the final
  contribution and the current CSF policy.
- Recheck that the main-matter label remains at or below page 12 after author
  and reviewer-driven revisions.

## What changed in this pass

- Reframed the paper around the decryption attack, construction, game chain,
  and checked conditional theorem.
- Put the one paid hop and all exact bridges in the main body.
- Added proof sketches for conditional KL preservation, integer Gaussians, and
  trace compilation.
- Reworked the logic section in the style of the CSF SSProve paper: three
  semantic judgments, a representative rules figure, the nonlinear soundness
  bridge, and a named local-to-adaptive theorem with an independent audit path.
- Added an explicit theorem-boundary table, trusted-base discussion, audit
  path, limitations, ethics statement, and AI-use disclosure.
- Converted the manuscript to anonymous IEEE conference format.
- Forced a clean dependency rebuild of the final Rocq theorem and recorded the
  measured environment and build time.
