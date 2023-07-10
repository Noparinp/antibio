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
drug_list = data.columns[4:].to_list()
print(drug_list)
data_length = len(data_df)

drug_df = data.iloc[:,4:]

# drug df data contains S R and np.nan
# count S R and np.nan of each colums of drug
col_names = ['name', 'S', 'R', 'None']
count_df = pd.DataFrame(columns=col_names)
count_df['name'] = drug_df.columns

'''
# fox = data_df['FOX'].value_counts()
# fox['None'] = data_length - fox['S'] - fox['R']
# # access to the value of fox column
# print(fox['S'])
# print(fox['R'])
# print(fox['None'])

'''
# the function is not working when there is no S or R in the column
# edit 

def count_S_R_None2(data,drug):
    data_length = len(data)
    count = data[drug].value_counts()
    if 'S' in count:
        count_s = count['S']
    else:
        count_s = 0
    if 'R' in count:
        count_r = count['R']
    else:
        count_r = 0
    count_none = data_length - count_s - count_r
    return count_s, count_r, count_none

print(count_S_R_None2(data_df,'AMX'))



for drug in drug_list:
    count_s, count_r, count_none = count_S_R_None2(data_df,drug)
    print(count_s, count_r, count_none)
    count_df.loc[count_df['name'] == drug, 'S'] = count_s
    count_df.loc[count_df['name'] == drug, 'R'] = count_r
    count_df.loc[count_df['name'] == drug, 'None'] = count_none

print(count_df.head(10))
count_df.to_csv("D:/AllResearch/R_learning/count_df_recent.csv", index=False)

##############################################################################

