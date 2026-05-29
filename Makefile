MAIN := main

LATEXMK := latexmk
LATEXMK_FLAGS := -xelatex -shell-escape -interaction=nonstopmode -halt-on-error

.PHONY: all clean

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex $(wildcard *.tex) reference.bib
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

clean:
	$(LATEXMK) -c $(MAIN).tex
	rm -rf _minted-$(MAIN)
