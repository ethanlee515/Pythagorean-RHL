# CSF 2027 readiness assessment

## Verdict

This project is a genuine CSF fit, not a fool's errand.  The venue explicitly
lists computer-aided cryptography and formal verification, and SSProve itself
is a CSF precedent.  The strongest defensible story is:

> A machine-checked good-execution IND-CPAD-to-IND-CPA reduction that preserves
> the parameter-critical square-root loss for adaptive decryption queries,
> together with reusable quantitative SSProve infrastructure.  Imperfect
> correctness is isolated as one standard up-to-bad transition.

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

1. **State the one-hop correctness extension precisely.**  The checked proof
   is the good-execution theorem.  For an execution-wide event
   <code>Bad_corr</code>, a standard up-to-bad transition adds
   <code>Pr[Bad_corr]</code> to the checked bound; the Pythagorean proof is
   unchanged.  An instantiation must either supply that aggregate probability
   directly or derive it from per-operation errors, in which case encryption
   and evaluation call counts must also be accounted for.  Do not describe
   this as a fully mechanized imperfect-correctness theorem yet, but also do
   not present it as a foundational obstacle.

2. **Concrete chart instantiation.**  Prove the origin-centered chart laws for
   at least one meaningful plaintext model, including wraparound and decoding.
   A worked instantiation would greatly strengthen both relevance and
   auditability even if a full CKKS implementation remains future work.

3. **Record the conventional PPT audit.**  SSProve's semantics check package
   behavior, not a runtime judgment; its published computational-security
   interpretation likewise places PPT in the metatheory.  The reduction here
   runs the adversary once, forwards calls, maintains polynomial-size tables,
   and samples the required Gaussians.  This short audit belongs in the paper,
   but extending SSProve with a cost semantics is not an obligation of this
   work.

4. **Position the inherited MathComp residue accurately.**  The current
   top-level dependency graph names
   <code>realsum.__admitted__interchange_psum</code> through SSProve's existing
   MathComp Analysis semantics.  This is not an unproved lemma introduced by
   Mending: <code>interchange_psum_proved</code> proves the exact statement
   locally, and its own <code>Print Assumptions</code> contains only the usual
   extensionality and choice principles.  The proof has been submitted as
   [MathComp Analysis PR #2007](https://github.com/math-comp/analysis/pull/2007),
   which is currently open and mergeable.  An upstream release is therefore a
   dependency-integration matter, not unfinished mathematics in this project.
   Keep the PR URL out of a double-blind manuscript or artifact if it would
   identify the authors.

5. **Independent proof audit.**  The development and manuscript are
   substantially AI-assisted.  Before submission, a human author should
   inspect the specification hot path, run <code>Print Assumptions</code> on
   an explicit functor instantiation, and spot-check the nontrivial compiler,
   summability, and game-bridge proofs.

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
- Added an explicit theorem-boundary table, trusted-base discussion, audit
  path, limitations, ethics statement, and AI-use disclosure.
- Converted the manuscript to anonymous IEEE conference format.
- Forced a clean dependency rebuild of the final Rocq theorem and recorded the
  measured environment and build time.
