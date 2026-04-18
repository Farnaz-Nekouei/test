def inject_tables(metrics, tex_path="reports/traffic_analysis_BW_BY.tex"):
    """
    Inject computed tables into LaTeX document.
    Replaces placeholder: % INSERT_TABLES_HERE
    """

    with open(tex_path, "r", encoding="utf-8") as f:
        tex = f.read()

    # -----------------------------
    # TABLE 1: BW vs BY
    # -----------------------------
    table1 = f"""
\\begin{{table}}[H]
\\centering
\\begin{{tabular}}{{lcc}}
\\toprule
Metric & BW & BY \\\\
\\midrule
Mean Speed (km/h) & {metrics['bw']['speed_mean']:.2f} & {metrics['by']['speed_mean']:.2f} \\\\
Mean Flow (veh/h) & {metrics['bw']['flow_mean']:.2f} & {metrics['by']['flow_mean']:.2f} \\\\
Congestion Index & {metrics['bw']['congestion_mean']:.2f} & {metrics['by']['congestion_mean']:.2f} \\\\
\\bottomrule
\\end{{tabular}}
\\caption{{Traffic comparison between Baden-Württemberg and Bayern}}
\\end{{table}}
"""

    # -----------------------------
    # TABLE 2: Correlations
    # -----------------------------
    table2 = f"""
\\begin{{table}}[H]
\\centering
\\begin{{tabular}}{{lc}}
\\toprule
Relationship & Correlation \\\\
\\midrule
Weather vs Congestion & {metrics['corr']['weather_congestion']:.2f} \\\\
Traffic vs Speed & {metrics['corr']['economic_traffic']:.2f} \\\\
Speed vs Flow & {metrics['corr']['speed_density']:.2f} \\\\
\\bottomrule
\\end{{tabular}}
\\caption{{Correlation structure of the traffic system}}
\\end{{table}}
"""

    # -----------------------------
    # Inject into LaTeX
    # -----------------------------
    if "% INSERT_TABLES_HERE" in tex:
        tex = tex.replace("% INSERT_TABLES_HERE", table1 + "\n" + table2)
    else:
        print("⚠️ WARNING: Placeholder not found in LaTeX file")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex)

    print("✅ Tables successfully injected into LaTeX")


# Optional backward compatibility
def export(metrics):
    return inject_tables(metrics)