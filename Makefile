DOCUMENTS := main arxiv_eprint
PDFS := $(addsuffix .pdf,$(DOCUMENTS))
ENTRYPOINTS := $(addsuffix .tex,$(DOCUMENTS))
TEX_SOURCES := $(filter-out $(ENTRYPOINTS),$(wildcard *.tex))

.DEFAULT_GOAL := all

LATEXMK := latexmk
LATEXMK_FLAGS := -xelatex -shell-escape -interaction=nonstopmode -halt-on-error
EXCERPT_ROOT := rocq-excerpts
EXCERPT_SRCS := \
	../theories/NextMessage/Trace.v \
	../theories/ProgramLogics/Ae.v \
	../theories/ProgramLogics/Pyth.v \
	../theories/ProgramLogics/PythCompile.v \
	../theories/Probability/DiscreteGaussians/DiscreteGaussian.v \
	../theories/Probability/DiscreteGaussians/DiscreteGaussianKL.v \
	../theories/LibExtras/MathcompExtras/DTuple.v \
	../theories/LibExtras/SSProveExtras/DiscreteGaussian.v \
	../theories/Schemes/ApproxFHE.v \
	../theories/Schemes/Utils/IntVec.v \
	../theories/Schemes/Indcpa.v \
	../theories/Schemes/Indcpad.v \
	../theories/Constructions/NoiseFlooding.v \
	../theories/Security/IndcpadSimulator.v \
	../theories/Security/NoiseFloodingSecurity/Prelude.v \
	../theories/Security/NoiseFloodingSecurity/Final.v

.PHONY: all clean refresh-formal-excerpts

all: $(PDFS)

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

$(PDFS): %.pdf: refresh-formal-excerpts %.tex $(TEX_SOURCES) reference.bib
	$(LATEXMK) $(LATEXMK_FLAGS) $*.tex

clean:
	$(LATEXMK) -c main.tex
	$(LATEXMK) -c arxiv_eprint.tex
	rm -rf $(addprefix _minted-,$(DOCUMENTS))
