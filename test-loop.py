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

print(data_df.head())
########################Prepare data #######################################################
# create dictionary for value s r or np.nan
drugs_dict = {'S': -1, 'R': 1, np.nan: 0}
# replace value in data_df
data_df.iloc[:, 4:32] = data_df.replace(drugs_dict)
print(data_df.head())



