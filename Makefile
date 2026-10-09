MAIN := main
ARXIV_MAIN := main-arxiv

LATEXMK := latexmk
LATEXMK_FLAGS := -xelatex -shell-escape -interaction=nonstopmode -halt-on-error
ARXIV_LATEXMK_FLAGS := -xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error
EXCERPT_ROOT := rocq-excerpts
EXCERPT_SRCS := \
	../theories/NextMessage/Trace.v \
	../theories/ProgramLogics/Ae.v \
	../theories/ProgramLogics/Pyth.v \
	../theories/ProgramLogics/PythCompile.v \
	../theories/Probability/DiscreteGaussians/DiscreteGaussian.v \
	../theories/Probability/DiscreteGaussians/DiscreteGaussianKL.v \
	../theories/LibExtras/MathcompExtras/DTuple.v \
	../theories/LibExtras/MathcompExtras/ListExtras.v \
	../theories/LibExtras/SSProveExtras/ChoiceVector.v \
	../theories/Probability/KL/Core.v \
	../theories/LibExtras/SSProveExtras/DiscreteGaussian.v \
	../theories/Schemes/ApproxFHE.v \
	../theories/Schemes/Utils/IntVec.v \
	../theories/Schemes/Indcpa.v \
	../theories/Schemes/Indcpad.v \
	../theories/Constructions/NoiseFlooding.v \
	../theories/Security/IndcpadSimulator.v \
	../theories/Security/NoiseFloodingSecurity/GaussianBasics.v \
	../theories/Security/NoiseFloodingSecurity/Prelude.v \
	../theories/Security/NoiseFloodingSecurity/Final.v

.PHONY: all csf arxiv arxiv-source clean refresh-formal-excerpts summarize-formal-excerpts

all: $(MAIN).pdf

csf: $(MAIN).pdf

arxiv: $(ARXIV_MAIN).pdf

arxiv-source: arxiv
	python3 scripts/package-arxiv.py

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

summarize-formal-excerpts: refresh-formal-excerpts
	python3 scripts/count-interface-excerpts.py --latex > formal-excerpt-size.tex

$(MAIN).pdf: summarize-formal-excerpts $(MAIN).tex $(wildcard *.tex) reference.bib
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

$(ARXIV_MAIN).pdf: summarize-formal-excerpts $(ARXIV_MAIN).tex $(wildcard *.tex) reference.bib
	$(LATEXMK) $(ARXIV_LATEXMK_FLAGS) $(ARXIV_MAIN).tex

clean:
	$(LATEXMK) -c $(MAIN).tex
	$(LATEXMK) -c $(ARXIV_MAIN).tex
	rm -rf _minted-$(MAIN) _minted-$(ARXIV_MAIN)
