import numpy as np
import seaborn
import pandas as pd
import matplotlib.pyplot as plt
import os


os.chdir("E:/Download_E/")
data = pd.read_excel("microbiology_data.xlsx")
data_df = pd.DataFrame(data)

organisms = data['organism']
spctypes = data['spctype']
drugs_df = data_df.iloc[:, 4:]


########################Prepare data #######################################################
# create dictionary for value s r or np.nan
drugs_dict = {'S': -1, 'R': 1, np.nan: 0}
# replace value in drugs_df
drugs_df = drugs_df.replace(drugs_dict)
# sum of each column in drug dataframe
drugs_sum = drugs_df.sum(axis=0) # type is series
#add drug  sum row at the end of data_df
data_df.loc['drug_sum'] = drugs_sum
# print(data_df.tail())


#plot the sum of each column with label value at each bar
# plt.figure(figsize=(10, 5))
# plt.bar(drugs_sum.index, drugs_sum.values)
# plt.xticks(rotation=90)
# plt.ylabel('Number of Isolates')
# plt.title('Number of Isolates Resistant to Each Antibiotic')
# plt.show()

########################################## data of each organism and specimen type##############################################
# iterate thright the spctypes and organism and sum the value from drug_df
# and create a new dataframe with the sum of each spctype and organism
# spc_org_df = pd.DataFrame()
# for spc in spctypes.unique():
#     for org in organisms.unique():
#         spc_org_df.loc[spc, org] = drugs_df[(spctypes == spc) & (organisms == org)].sum().sum()
    

# print(spc_org_df.head())
# spc_org_df.to_csv('D:/AllResearch/R_learning/spc_org_df.csv')

#########################################################################################
# iterate thright the spctypes and organism and sum the value from drug_df 
# and create a new dataframe with the sum of each spctype and organism and drug
spc_org_drug_df = pd.DataFrame()
for spc in spctypes.unique():
    for org in organisms.unique():
        for drug in drugs_df.columns:
            spc_org_drug_df.loc[spc, org, drug] = drugs_df[(spctypes == spc) & (organisms == org)][drug].sum()

print(spc_org_drug_df.head())
spc_org_drug_df.to_csv('D:/AllResearch/R_learning/spc_org_drug_df.csv')


    









       


