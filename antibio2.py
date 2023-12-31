import numpy as np
import seaborn
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt
import seaborn as sns


os.chdir("E:/Download_E/")
data = pd.read_excel("microbiology_data.xlsx")
data_df = pd.DataFrame(data)

organisms = data['organism']
spctypes = data['spctype']
data_df = data_df.drop(columns=['spcdate','hn'])

######################## Prepare data #######################################################
# create dictionary for value s r or blank cell
drugs_dict = {'S': -1, 'R': 1, '': 0}
# replace value in data_df
data_df= data_df.replace(drugs_dict)

#convert to list
druglist = (data_df.columns[3:]).tolist()

####################### Process data ########################################################
'''
count the number of test for each spctype, organism, and drug and sum the value of resistance
example: nuber of resistance test of Streptococcus pneumoniae in blood to Ampicillin is 2
'''

# spc_org_drug_df = pd.DataFrame(columns=['spctype', 'organism', 'drug', 'sum_value', 'test_count', 'resistance_rate'])

# for spc in spctypes.unique():
#     for org in organisms.unique():
#         for drug in druglist:
#             sum_value = data_df.loc[(spctypes == spc) & (organisms == org), drug].sum()
#             test_count = data_df.loc[(spctypes == spc) & (organisms == org), drug].count()
#             resistance_rate = sum_value/test_count
#             spc_org_drug_df = spc_org_drug_df.append({'spctype': spc, 'organism': org, 'drug': drug, 'sum_value': sum_value, 'test_count': test_count, 'resistance_rate': resistance_rate}, ignore_index=True)

# # save the dataframe to csv file
# spc_org_drug_df.to_csv("D:/AllResearch/R_learning/spc_org_drug_df_new.csv", index=False)

####################################################################################################

# read the dataframe from csv file
spc_org_drug= pd.read_csv("D:/AllResearch/R_learning/spc_org_drug_df_new.csv")
spc_org_drug_df = pd.DataFrame(spc_org_drug)

spc_org_drug_df['marker'] = 'circle'  # Initialize all markers as circles
spc_org_drug_df.loc[spc_org_drug_df['resistance_rate'] < 0, 'marker'] = 'triangle'  # Set marker as triangle for negative resistance rate



plt.figure(figsize=(10, 10))

sns.scatterplot(x='drug', y='organism', hue='resistance_rate', style='marker', size='resistance_rate',
                markers={'circle': 'o', 'triangle': '^'}, alpha = 0.5,sizes=(100, 500), data=spc_org_drug_df)
# move legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()
plt.gca().set_axisbelow(True)


# caalculate the average resistance rate of each drug
avg_resistance_rate = spc_org_drug_df.groupby('drug')['resistance_rate'].mean()
avg_resistance_rate = avg_resistance_rate.reset_index()
avg_resistance_rate = avg_resistance_rate.sort_values(by='resistance_rate', ascending=False)
print(avg_resistance_rate)

#plot the scatter sort by the lowest resistance rate to the highest type of drug 
plt.figure(figsize=(10, 10))
sns.scatterplot(x='drug', y='organism', hue='resistance_rate', style='marker', size='resistance_rate',
                markers={'circle': 'o', 'triangle': '^'}, alpha = 0.5,sizes=(100, 500), data=spc_org_drug_df)
# move legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()

plt.gca().set_axisbelow(True)
# add the average resistance rate of each drug to the plot under the x-axis of each drug name
for i in range(len(avg_resistance_rate)):

    plt.text(i, 19, round(avg_resistance_rate['resistance_rate'][i], 2), ha='center', va='top', fontsize=10)



plt.show()









