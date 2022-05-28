all: \
	reports/factorizacion_numeros_primos.pfd

define renderLatex
    cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
endef

reports/factorizacion_numeros_primos.pfd: reports/factorizacion_numeros_primos.tex
	$(renderLatex)


clean:
	rm --force --recursive reports/pythontex*
	rm --force reports/*.aux
	rm --force reports/*.out
	rm --force reports/*.log
	rm --force reports/*.pdf
	rm --force reports/*.pytxcode

