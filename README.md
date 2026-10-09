# Pythagorean RHL manuscript

The section files, mathematical macros, bibliography, and Rocq excerpts are
shared by both formats. Build from this directory:

```sh
make csf          # main.pdf: anonymous IEEE/CSF conference format, two columns
make arxiv        # main-arxiv.pdf: named 11pt article, one column, A4, 1in margins
make arxiv-source # arxiv-source.zip: self-contained public source bundle
```

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
| `\CameraReady` | Show names, affiliations, artifact links, and funding acknowledgments. |
| `\Draft` | Show author notes and Alex's alternative introduction. |
| `\NoShellEscape` | Render code without running Pygments. |

The switches are independent. For example, `\CameraReady` alone gives named
authors in CSF format; `\SingleColumn` alone gives an anonymous article.
`main-arxiv.tex` enables `\SingleColumn`, `\CameraReady`, and `\NoShellEscape`.
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
