# Overleaf reconciliation, 2026-10-09

Compared the canonical manuscript at commit `a23c4cd` with
`../Pythagorean_RHL_arxiv_version.zip`. Archive export timestamps were not used
to determine which content is newer; the Git history and source differences
were used instead.

All 16 Rocq files present in both versions are byte-identical. The substantive
sections on the construction, reduction, program logic, compiler, related work,
conclusion, and other appendices are also identical.

| Difference | Resolution |
| --- | --- |
| Git has the excerpt-size table, specification-helper subsection, and four additional Rocq files added in `a23c4cd`; the ZIP omits them. | Retained all Git additions, their generated counts (724 lines, 39 listings, 16 files), and the discussion referencing the table. |
| ZIP uses an 11pt article with A4 paper and one-inch margins, named authors with affiliation/email footnotes, no date, and `\appendix`. | Added `\SingleColumn` with class-specific authors, keywords, and appendix commands. Public entry point is `main-arxiv.tex`; default `main.tex` uses IEEE/CSF. Both are camera-ready. |
| ZIP removes the oversized title subtitle and uses “We machine-check” in the abstract. | Adopted both in the shared manuscript. |
| ZIP inlines the mathematical macros in `main.tex` and removes draft note commands. | Kept one shared `macros.tex`, preserved draft notes and the optional alternative introduction, and moved configuration before the class into `paper-options.tex`. |
| ZIP adds funding and combines it with the same AI disclosure. | Added the funding text verbatim; both formats show one Acknowledgments section containing both funding and AI disclosure, each exactly once. |
| ZIP omits the ethics section. | Retained it in both formats to preserve the canonical content. |
| ZIP rephrases the AI-assisted line-count caveat. | Adopted its wording. |
| ZIP adds an artifact link to the introduction and changes the repository URL's capitalization elsewhere. | Added the introduction link unconditionally; kept the canonical lowercase URL consistently. |
| ZIP shortens the inherited assumption's name by removing `realsum.`. | Kept the more precise qualified name; made it breakable in the article format without changing the printed identifier. |
| ZIP scales the theory-map figure to the available width, adds line breaks, and anchors lane labels above their nodes. | Adopted the complete figure and its `adjustbox` dependency in both formats. |
| ZIP substitutes JuliaMono for FreeMono's missing double-brace glyphs. | Ported both Unicode mappings, keeping JuliaMono optional with a FreeSerif fallback. The ZIP contains no bundled fonts. |
| ZIP rewrites one bibliography entry using literal `ü` and different whitespace/bracing. | Kept the same bibliographic content with Git's portable BibTeX escape `Sch{\"u}rmann`. |

The exported ZIP still loads ordinary minted and therefore does not itself
provide a build without shell escape. Added a separate `\NoShellEscape` mode
and enabled it for the public entry point, so restricted builds use plain
listings rather than invoking Pygments. A generated source archive flattens the
wrapper into `main.tex` and includes `main.bbl` and every checked-in excerpt.
This is a local compatibility measure; an actual ArXiv server build has not
been tested.

Validated with the installed TeX Live 2023:

- `make csf arxiv-source` succeeds: the default CSF PDF has 25 pages and the
  public article has 41 pages.
- Both formats include named authors, funding, AI disclosure, and the ethics
  section. The former author-visibility switch and its conditional branches
  have been removed at the authors' request.
- The extracted submission ZIP compiles in a fresh temporary directory with
  `-no-shell-escape`, without a minted cache or the parent repository.
- The final builds have resolved references/citations, both Rocq brace
  glyphs, the 724-line excerpt count, and no overfull-box or missing-character
  warnings. Title pages and the theory-map figure were visually inspected.
- All 16 Rocq files shared with the input ZIP remain byte-identical, and
  `git diff --check` passes.

Existing IEEEtran/fontspec font-shape substitutions and minted's
shell-disabled platform warning remain benign local compiler warnings.

## Git merge recovery

Resolved the merge of `fd0abb04` (the ZIP reconciliation) into `main` at
`0be1509` (the existing Overleaf integration). Kept the excerpt-count additions,
portable font fallback, restricted-build mode, and source packager. The
single-column version uses `main-arxiv.tex` as its sole entry point, sharing
the manuscript with `main.tex`. The default `make` builds both formats. Funding
and AI disclosure use a single shared Acknowledgments section, and all author
names and identifying links are unconditional in both layouts.
