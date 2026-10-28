# Pythagorean RHL manuscript

**Verified Pythagorean Composition for Adaptive Cryptographic Games: Noise
Flooding in Homomorphic Encryption** has been accepted at **CSF 2027**. This
repository is preparing the camera-ready manuscript and its public arXiv
version. It is also the `Pythagorean-RHL/` submodule of the
[Mending formal artifact](https://github.com/ethanlee515/mending).
Both formats include named authors, affiliations, artifact links, and funding;
the anonymous/camera-ready switch has been removed.

Contributor context: preserve this public, named-author configuration. Keep
dependency versions and trusted-base statements synchronized with Mending's
`mending.opam` and README.

The artifact now checks with Rocq 9.0.1, MathComp 2.6.0, MathComp Analysis and
experimental reals 1.18.0, and SSProve's `main` branch. The revision used for
this upgrade is `9a37fe0ab79d041f8d835e6cf18e37614b16a791`; see
[Mending's setup and snapshot instructions](https://github.com/ethanlee515/mending#setup).
[SSProve PR #124](https://github.com/SSProve/ssprove/pull/124) is merged, and
our summation proofs from
[Analysis PR #2007](https://github.com/math-comp/analysis/pull/2007) are used
through the upgraded dependency stack. Duplicate local compatibility proofs
have been removed. MathComp's built-in ring tactic replaces the separate
algebra-tactics package. The complete artifact rebuild and top-level
assumption audit passed on October 28, 2026; the audit contains no admitted
summation lemma. Rebuild the full artifact and rerun the audit whenever
advancing the moving SSProve branch.

The section files, mathematical macros, bibliography, and Rocq excerpts are
shared by both formats. Build from this directory:

```sh
make csf          # main.pdf: camera-ready IEEE/CSF conference format, two columns
make arxiv        # main-arxiv.pdf: named 11pt article, one column, A4, 1in margins
make arxiv-source # arxiv-source.zip: self-contained public source bundle
```

All formats include named authors, affiliations, artifact links, and funding.
`make` builds both formats using `main.tex` and `main-arxiv.tex`.

Both builds use XeLaTeX and BibTeX through `latexmk`. CSF additionally uses
Pygments (`pygmentize`) for syntax highlighting. The ArXiv entry point disables
shell escape and uses minted's plain listing renderer, preserving the code,
Unicode symbols, line ranges, numbering, and wrapping without a highlighting
cache. This mode affects listings only; it is independent of author draft mode.

For Overleaf, choose `main.tex` or `main-arxiv.tex` as the main document and
XeLaTeX as the compiler. The article format can also be used for a Crypto draft;
it is a generic article layout, not a venue-specific submission template.

`paper-options.tex` is read before the document class. Uncomment its switches
to configure a direct `main.tex` build:

| Macro | Effect when defined |
| --- | --- |
| `\SingleColumn` | Use the article layout instead of IEEEtran conference layout. |
| `\Draft` | Show author notes and Alex's alternative introduction. |
| `\NoShellEscape` | Render code without running Pygments. |

The switches control format, author notes, and code rendering independently.
`main-arxiv.tex` enables `\SingleColumn` and `\NoShellEscape`.
It also includes a table of contents after the abstract; the conference
version has no table of contents.
Use XeLaTeX without `-shell-escape` whenever `\NoShellEscape` is enabled.

The document uses TeX Gyre Termes/Heros, DejaVu Sans Mono, and FreeMono. The two
Rocq glyphs `⦃` and `⦄` use JuliaMono if available, otherwise FreeSerif. JuliaMono
is optional and does not need to be installed or bundled.

The Makefile refreshes the checked-in Rocq excerpts from `../theories/` when
available, then regenerates `formal-excerpt-size.tex`. An isolated manuscript
checkout uses its checked-in excerpts. Run `make` again after changing listing
ranges to update the table. The submission ZIP includes these sources, the
generated table, and `main.bbl`; its single entry point is `main.tex`. It can be
compiled after extraction without the parent repository, Make, Python, shell
escape, or Pygments. The ZIP is generated and ignored by Git.

See [MERGE-NOTES.md](MERGE-NOTES.md) for the reconciliation with the Overleaf
export and the remaining local compiler warnings.
