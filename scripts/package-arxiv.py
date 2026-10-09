#!/usr/bin/env python3
"""Package the public manuscript without requiring Make, Python, or Pygments."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    bibliography = ROOT / "main-arxiv.bbl"
    if not bibliography.is_file():
        raise SystemExit("Build the public version first with make arxiv.")
    # Flatten the wrapper so there is exactly one compilation entry point.
    wrapper = (ROOT / "main-arxiv.tex").read_text()
    manuscript = wrapper.replace("\\input{main}", (ROOT / "main.tex").read_text())
    destination = ROOT / "arxiv-source.zip"
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("main.tex", manuscript)
        for source in sorted(ROOT.glob("*.tex")):
            if source.name not in {"main.tex", "main-arxiv.tex", "arxiv_eprint.tex"}:
                archive.write(source, source.name)
        archive.write(ROOT / "reference.bib", "reference.bib")
        archive.write(bibliography, "main.bbl")
        for source in sorted((ROOT / "rocq-excerpts").rglob("*.v")):
            archive.write(source, source.relative_to(ROOT))
    print(destination)


if __name__ == "__main__":
    main()
