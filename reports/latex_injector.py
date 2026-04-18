import os

def inject_figures(tex_path, figures_dir="reports/figures"):
    """
    Automatically inject all PNG figures into LaTeX paper
    """

    figs = sorted([f for f in os.listdir(figures_dir) if f.endswith(".png")])

    injection = "\n\\section{Auto-Generated Figures}\n"

    for f in figs:
        injection += f"""
\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.9\\textwidth]{{figures/{f}}}
\\end{{figure}}
"""

    with open(tex_path, "a") as file:
        file.write(injection)

    print("LaTeX figures injected automatically.")