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

# print(data_df.head())

drugs_df = data_df.iloc[:, 4:]
# print(drugs_df.head())

# print unique value in all drugs_df
# for i in range(0, len(drugs_df.columns)):
    # print(drugs_df.iloc[:, i].unique())
# result ['S' 'R' nan]

# # if value is 'S' or 'R' then replace with -1 or 1 else 0
# for i in range(0, len(drugs_df.columns)):
#     drugs_df.iloc[:, i] = drugs_df.iloc[:, i].replace('S', -1)
#     drugs_df.iloc[:, i] = drugs_df.iloc[:, i].replace('R', 1)
#     drugs_df.iloc[:, i] = drugs_df.iloc[:, i].replace(np.nan, 0)

# create dictionary for value s r or np.nan
drugs_dict = {'S': -1, 'R': 1, np.nan: 0}
# replace value in drugs_df
drugs_df = drugs_df.replace(drugs_dict)
# print(drugs_df.head())

# calculate summation of each drug column of each organism and each spctype
# example for organism 'Acinetobacter baumannii' and spctype 'Blood' and drug 'Amikacin' summation is 0
print(data_df.groupby(['organism', 'spctype']).sum())

       


