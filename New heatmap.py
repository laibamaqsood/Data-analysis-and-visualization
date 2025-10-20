import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# # Define your new data
data_new = {
    'Genes': [
        'collagen type VI alpha 3 chain',
        'signal transducer and activator of transcription 1',
        'collagen type IV alpha 2 chain',
        'epithelial cell transforming 2',
        'BICD cargo adaptor 1',
        'kinesin family member 3A',
        'transforming growth factor beta induced',
        'denticleless E3 ubiquitin protein ligase homolog',
        'collagen type I alpha 1 chain',
        'solute carrier family 4 member 2',
        'heat shock protein family D (Hsp60) member 1',
        'selectin E',
        'CD46 molecule',
        'RecQ like helicase',
        'drebrin 1',
        'solute carrier family 39 member 6',
        'phosphoserine aminotransferase 1',
        'TNF receptor superfamily member 10b',
        'nucleoporin 58',
        'EPH receptor B2',
        'heat shock protein family A (Hsp70) member 4',
        'tweety family member 3',
        'GINS complex subunit 4',
        'growth differentiation factor 15',
        'C-X-C motif chemokine ligand 1',
        'BUB1 mitotic checkpoint serine/threonine kinase',
        'formin like 2',
        'ectodermal-neural cortex 1',
        'cathepsin B',
        'Myb/SANT DNA binding domain containing 4 with coiled-coils',
        'apolipoprotein L domain containing 1',
        'collagen type XI alpha 1 chain',
        'pleckstrin homology like domain family A member 1',
        'proteasome activator subunit 3',
        'stanniocalcin 1',
        'annexin A6',
        'prolyl 3-hydroxylase 1',
        'ATP binding cassette subfamily F member 2',
        'glucose-6-phosphate dehydrogenase',
        'stress induced phosphoprotein 1',
        'PAT1 homolog 1, processing body mRNA decay factor',
        'glutathione peroxidase 8 (putative)',
        'acidic nuclear phosphoprotein 32 family member E',
        'trafficking kinesin protein 2',
        'sacsin molecular chaperone',
        'sorting nexin 10',
        'zyxin',
        'collagen type XVIII alpha 1 chain',
        'collagen triple helix repeat containing 1',
        'TIMP metallopeptidase inhibitor 1',
        'ELOVL fatty acid elongase 5',
        'lysyl oxidase like 2',
        'nucleolar and coiled-body phosphoprotein 1',
        'potassium inwardly rectifying channel subfamily J (8,15,15)'
    ],
    'GC': [-2.5974206, -2.05447582, -2.20608369, -1.00953309, -1.7394236, -1.24183663, -1.59145496, -1.06577493, -4.30007157, -1.75775788, -2.29757705, -2.04733426, -1.582118, -1.12273714, -1.16540072, -1.83167498, -1.06533922, -1.17127315, -1.60458874, -1.62368595, -2.00639461, -1.12822743, -1.23519366, -1.07349859, -1.92850098, -1.66414484, -2.94659914, -1.74639854, -1.08185035, -1.04906782, -2.70260444, -2.88828686, -1.33262191, -2.08960536, -1.99818432, -1.43224994, -1.26405866, -1.76876956, -1.01912509, -1.05587084, -1.17254814, -1.62693304, -2.48033766, -1.12033115, -1.19005553, -1.89028238, -2.84076015, -1.64456306, -3.51622428, -2.06201638, -1.14238058, -1.50117412, -1.12579208, -2.41200186],
    'PC': [-1.2893941, -0.608964, 0.8659641, -1.1962026, -0.4968344, -0.6991537, -1.2158817, -0.4831512, -3.1338336, 0.4557823, -1.1083246, -1.8954125, -0.872711, -0.8889124, 0.5690306, -0.7018896, -0.4783727, -0.4353357, -0.4216852, -0.715947, -0.4280029, 0.4641235, -0.8783255, -0.5575187, 0.9576476, -0.6030976, -0.9113759, 0.5240091, -0.8858768, -1.4376665, 0.9982885, -1.3939214, -0.3217452, 0.3179534, -1.1001656, -1.0973202, 0.3486188, 0.6859895, 0.7748379, 0.5418105, 0.5422527, -0.9993387, -1.1146919, -0.675521, -1.8371723, -0.7478759, 0.8996875, -0.4873017, -4.0324772, 0.7071924, -0.6078166, -0.5663352, -0.8398027, -6.5119059],
    'CRC': [-1.1644593, -2.033336, -1.2311015, -2.8313262, -1.0111083, -1.2658913, -1.5410205, -2.0595083, -2.2810499, -1.5525161, -1.4806327, -3.2244576, -1.1667288, -1.0693532, -1.7790942, -1.9480353, -5.0887804, -1.3597857, -1.150494, -1.5677864, -1.2128065, -1.422166, -2.8342285, -1.5085642, -2.4110984, -2.7314605, -1.1790182, -1.8975907, -1.5392837, -1.4727749, -1.8227777, -3.1629018, -1.9879338, -1.1645385, -2.4338166, -1.0585784, -1.163993, -1.2933261, -1.9560884, -2.0833434, -1.0041326, -1.3088999, -1.4349689, 0.9313763, -2.1486541, -1.9155475, -1.04196, -1.5544317, -1.5599254, -1.855739, -1.4675078, -1.5387193, -1.6646836, -2.7498428]
}
df = pd.DataFrame(data_new)

# Create a clustermap
# clustermap = sns.clustermap(df.set_index('Genes'), cmap="coolwarm", annot=False, fmt=".2f", cbar_kws={'label': 'log2FC', 'shrink': 0.5},
#                             method='average', col_cluster=False, figsize=(12, 6), cbar_pos=(0.95, 0.25, 0.02, 0.5))


# Adjust y-axis labels rotation
clustermap = sns.clustermap(df.set_index('Genes'), cmap="crest", annot=False, fmt=".2f", 
                            cbar_kws={'label': 'log2FC', 'shrink': 0.5},
                            method='average', col_cluster=False, figsize=(8, 22),
                            cbar_pos=(0.80, 0.2, 0.02, 0.5))  # Adjust these values as needed

# Adjust the y-axis labels rotation if needed
plt.setp(clustermap.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)

# Set the x-axis label
clustermap.ax_heatmap.set_xlabel('Datasets', fontsize=12, labelpad=4, ha='center')

# Set the y-axis label
clustermap.ax_heatmap.set_ylabel('Genes',labelpad=5, fontsize=10)
plt.ylabel('log2FC', fontsize=10)
clustermap.ax_heatmap.set_yticklabels(clustermap.ax_heatmap.get_yticklabels(), fontsize=6)
# Show the plot
plt.show()