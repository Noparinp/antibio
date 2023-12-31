import numpy as np
import seaborn
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.chdir("E:/Download_E/")
data = pd.read_excel("microbiology_data.xlsx")
data_df = pd.DataFrame(data)

organisms = data['organism']
spctypes = data['spctype']
data_df = data_df.drop(columns=['spcdate','hn'])
print(data_df.head())
########################Prepare data #######################################################
# create dictionary for value s r or blank cell
drugs_dict = {'S': -1, 'R': 1, '': 0}
# replace value in data_df
data_df= data_df.replace(drugs_dict)
# drop specdate column



druglist = data_df.columns[3:]
print(druglist)
#convert to list
druglist = druglist.tolist()

u_spctype = spctypes.unique()
u_organism = organisms.unique()
#################################################################################################
# Create a data frame for the sum of each spctype, organism, and drug

# spc_org_drug_df = pd.DataFrame(columns=['spctype', 'organism', 'drug', 'sum_value'])

# for spc in u_spctype:
#     for org in u_organism:
#         for drug in druglist:
#             sum_value = data_df.loc[(spctypes == spc) & (organisms == org), drug].sum()
#             spc_org_drug_df = spc_org_drug_df.append({'spctype': spc, 'organism': org, 'drug': drug, 'sum_value': sum_value}, ignore_index=True)

################################################################################################
spc_org_drug= pd.read_csv("D:/AllResearch/R_learning/spc_org_drug_df2.csv")
spc_org_drug_df = pd.DataFrame(spc_org_drug)
##################################### use specimen type as a main topic############################################

# #plot heatmap of sum of each spctype, organism, and drug


# # Filter the data based on column 'a' == 'yes'
# filtered_data = spc_org_drug_df[spc_org_drug_df['spctype'] == 'csf']

# # Pivot the filtered data to create a matrix for the heatmap
# heatmap_data = filtered_data.pivot(index='organism', columns='drug', values='sum_value')
############################################################################################

max_value = np.max(spc_org_drug['sum_value'])
min_value = np.min(spc_org_drug['sum_value'])
center = (max_value+min_value)/2


for drug in druglist:
   
    filtered_data = spc_org_drug_df[spc_org_drug_df['drug'] == drug]

    # Pivot the filtered data to create a matrix for the heatmap
    heatmap_data = filtered_data.pivot(index='organism', columns='spctype', values='sum_value')


    fig, ax = plt.subplots(figsize=(8, 10))  # Adjust the figure size as needed
    sns.set(font_scale=1.4)
    sns.heatmap(heatmap_data, annot=False, cmap='RdBu', ax=ax, linewidth=0.5, linecolor='black', square=True, center = center, vmax = max_value, vmin = min_value, cbar_kws={"shrink": 0.5})

    # Rotate the x-axis tick labels
    plt.xticks(rotation=45)  # Adjust the rotation angle as needed
    
    # Set labels and title
    plt.xlabel('Specimen type')
    plt.ylabel('Organism')
    plt.title(f'Heatmap of the {drug} resistance level of each organism ')

    # Show the plot
    plt.savefig(f'D:/AllResearch/R_learning/antibio_plot/drug/{drug}.png')
    plt.show()
    
    # SAVE IMAGE 

