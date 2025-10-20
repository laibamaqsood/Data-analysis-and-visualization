import matplotlib.pyplot as plt
import numpy as np

# Data from the table
terms = [
    "GnRH secretion", "Cholinergic synapse", "Gastric acid secretion", "ECM-receptor interaction",
    "Oxytocin signaling pathway", "Morphine addiction", "Circadian entrainment",
    "AGE-RAGE signaling pathway in diabetic complications", "Serotonergic synapse", "Dopaminergic synapse"
]
p_values = [
    6.67E-08, 6.64E-07, 1.47E-05, 2.28E-05, 1.21E-04, 1.55E-03, 1.75E-03, 1.86E-03, 2.37E-03, 3.22E-03
]
overlap_genes = [
    ["KCNJ5", "KCNJ6", "KCNJ11", "SPP1"], ["KCNJ6", "KCNJ12", "KCNQ1", "KCNQ3"], ["KCNJ10", "KCNQ1", "KCNJ1"],
    ["FN1", "SPP1", "CD44"], ["KCNJ5", "KCNJ6", "KCNJ12"], ["KCNJ5", "KCNJ6"], ["KCNJ5", "KCNJ6"],
    ["SERPINE1", "FN1"], ["KCNJ5", "KCNJ6"], ["KCNJ5", "KCNJ6"]
]

# Calculate -log10(p-values)
log_p_values = -np.log10(p_values)

# Calculate the size of the dots (number of overlap genes)
sizes = [len(genes) * 100 for genes in overlap_genes]  # Multiply by 100 for better visualization

# Create the dot plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(log_p_values, terms, s=sizes, c=p_values, cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5)
plt.colorbar(scatter, label='p-value')
plt.xlabel('-log10(p-value)')
plt.title('Dot Plot of Terms vs. -log10(p-value)')

# Annotate the dots with the number of overlap genes
for i, term in enumerate(terms):
    plt.text(log_p_values[i], term, str(len(overlap_genes[i])), fontsize=9, ha='right')

plt.gca().invert_yaxis()  # Invert y-axis to have the first term at the top
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
