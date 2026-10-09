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
`mending.opam` and README. Long dependency rebuilds are run by the user outside
the agent session during this preparation.

The dependency upgrade is deferred: the artifact retains the checked upstream
Rocq 9.0.1 / MathComp Analysis 1.16.0 stack. Our summation proof is merged into
newer Analysis, but adopting it requires MathComp 2.6 and compatible SSProve
support. As checked on October 9, 2026,
[SSProve PR #124](https://github.com/SSProve/ssprove/pull/124) is still unmerged
and its dependency bounds need updating. See the
[Mending dependency blocker](https://github.com/ethanlee515/mending#dependency-upgrade-blocker).
The current security theorem therefore still inherits the admitted summation
assumption. Revisit the upgrade when upstream support is available; an
author-maintained SSProve fork is a deferred option if the camera-ready deadline
requires it. Do not switch to an unmerged PR snapshot or claim that the inherited
assumption has disappeared. A future upgrade requires a full rebuild and
assumption audit before updating the manuscript's claims.

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
