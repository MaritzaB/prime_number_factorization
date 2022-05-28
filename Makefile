all: \
	reports/factorizacion_numeros_primos.pfd

.PHONY: \
	all \
	clean \
	format \
	tests

define renderLatex
    cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
endef

reports/factorizacion_numeros_primos.pfd: reports/factorizacion_numeros_primos.tex
	$(renderLatex)

clean:
	rm --force --recursive reports/pythontex*
	rm --force reports/*.aux
	rm --force reports/*.log
	rm --force reports/*.out
	rm --force reports/*.pdf
	rm --force reports/*.pytxcode
	rm --recursive --force __pycache__
	rm --recursive --force .pytest_cache
	rm --recursive --force */__pycache__

format:
	black --line-length 100 src/*.py


tests:
	pytest --verbose tests/