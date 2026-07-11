MAIN := main

LATEXMK := latexmk
LATEXMK_FLAGS := -xelatex -shell-escape -interaction=nonstopmode -halt-on-error
EXCERPT_ROOT := rocq-excerpts
EXCERPT_SRCS := \
	../theories/Schemes/ApproxFHE.v \
	../theories/Schemes/Indcpa.v \
	../theories/Schemes/Indcpad.v \
	../theories/Constructions/NoiseFlooding.v \
	../theories/Security/IndcpadSimulator.v \
	../theories/Security/NoiseFloodingSecurity/Prelude.v \
	../theories/Security/NoiseFloodingSecurity/Final.v

.PHONY: all clean refresh-formal-excerpts

all: $(MAIN).pdf

refresh-formal-excerpts:
	@for src in $(EXCERPT_SRCS); do \
		dst="$(EXCERPT_ROOT)/$${src#../}"; \
		if [ -f "$$src" ]; then \
			mkdir -p "$$(dirname "$$dst")"; \
			cp -p "$$src" "$$dst"; \
		elif [ ! -f "$$dst" ]; then \
			echo "missing $$src and $$dst"; \
			exit 1; \
		fi; \
	done

$(MAIN).pdf: refresh-formal-excerpts $(MAIN).tex $(wildcard *.tex) reference.bib
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

clean:
	$(LATEXMK) -c $(MAIN).tex
	rm -rf _minted-$(MAIN)
