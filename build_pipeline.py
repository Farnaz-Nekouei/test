import os
import subprocess
from reports.latex_injector import inject_figures
from reports.bib_generator import generate_bibtex

def build():

    print("\n🚀 BUILDING FULL IEEE RESEARCH PIPELINE\n")

    # 1. generate bibtex
    generate_bibtex()

    # 2. inject figures into latex
    inject_figures("reports/paper.tex")

    # 3. compile latex
    subprocess.run("pdflatex -interaction=nonstopmode reports/paper.tex", shell=True)
    subprocess.run("bibtex reports/paper", shell=True)
    subprocess.run("pdflatex reports/paper.tex", shell=True)
    subprocess.run("pdflatex reports/paper.tex", shell=True)

    print("\n✅ IEEE PAPER GENERATED\n")

if __name__ == "__main__":
    build()