import pandas as pd
import numpy  as np
import os

os.chdir("E:/Download_E/")
data = pd.read_excel("microbiology_data.xlsx")
data_df = pd.DataFrame(data)

###########################################################
# get unique value of organism and drug
org = data_df['organism'].unique()
print('org', org)
drug = data_df.columns[4:].to_list()
spctype = data_df['spctype'].unique()


# check function
count_r, count_s = data.loc[data['organism'] == 'Acinetobacter baumannii', 'GM'].value_counts()
print(count_r)
print(count_s)


####################################################################
def count_S_R_None_org(data,drug,org_col_name,desired_org):
    data_length = len(data)
    # org_list = data[org_col_name].unique()
    count = data.loc[data[org_col_name] == desired_org, drug].value_counts()
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

# try

count = count_S_R_None_org(data_df,'FOX','organism','Acinetobacter baumannii')
print('test: ',count)

##########################################################################
count_df = pd.DataFrame(columns=['name', 'organism','S', 'R', 'None'])

# fill name and organism column
# exammple name = AMX, organism = Acinetobacter baumannii
#          name = AMX, organism = Escherichia coli ....

for d in drug:
    for o in org:
        count_df = count_df.append({'name': d, 'organism': o}, ignore_index=True)

print('count df prepared')
print(count_df.head(10))

# Prepare data

# for d in drug:
#     for o in org:
#         count_s, count_r, count_none = count_S_R_None_org(data_df,d,'organism',o)
#         count_df.loc[(count_df['name'] == d) & (count_df['organism'] == o), 'S'] = count_s
#         count_df.loc[(count_df['name'] == d) & (count_df['organism'] == o), 'R'] = count_r
#         count_df.loc[(count_df['name'] == d) & (count_df['organism'] == o), 'None'] = count_none

# print(count_df.head(10))
# count_df.to_csv("D:/AllResearch/R_learning/count_df_rsn_of_drug_org1.csv", index=False)
# print('count df saved')
############################################################################################

#read file
os.chdir("D:/AllResearch/R_learning/")
count = pd.read_csv("count_df_rsn_of_drug_org1.csv")
count_df = pd.DataFrame(count)

# calculate rate of R
count_df['rate_r'] = count_df['R']/(count_df['S']+count_df['R'])
print(count_df.head(10))

#plot heatmap
import seaborn as sns
import matplotlib.pyplot as plt

# plot heat map by using pivot table
# pivot table
# index = organism
# columns = drug
# values = rate_r

heatmap_data = count_df.pivot(index='organism', columns='name', values='rate_r')
print(heatmap_data.head(10))

# plot heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(data=heatmap_data, annot=True, fmt='.1f', linewidths=.5, cmap='RdYlGn_r', linecolor='black', square=True)
plt.xlabel('Drug')
plt.ylabel('Organism')
plt.title('Heatmap of resistance rate of each drug and organism')

# add side title of color bar
plt.gcf().axes[0].yaxis.get_label().set_visible(True)
plt.gcf().axes[0].set_ylabel('Resistance rate')

plt.show()

'''
# find what drug with what organism has the top 10 highest resistance rate from heat_map data frame 
# example organism a and drug x has resistance rate y

'''
count_df['experiment_times'] = count_df['S'] + count_df['R']
print(count_df.head(10))
print('exper times added')
sorted_count_df = count_df.sort_values('rate_r', ascending=False)
top_10 = sorted_count_df.head(10)


# Print the top 10 rows with organism and drug information
for index, row in top_10.iterrows():
    organism = row['organism']
    drug = row['name']
    rate_r = row['rate_r']
    # add the number of experiment times 
    experiment_times = row['experiment_times']
    print('organism: ', organism, 'drug: ', drug, 'rate_r: ', rate_r, 'experiment_times: ', experiment_times)

#top 5 lowest resistance rate with highest experiment times
sorted_count_df = count_df.sort_values(['rate_r','experiment_times'], ascending=[True,False])
top_10 = sorted_count_df.head(10)
print('top 10 lowest resistance rate with highest experiment times')
for index, row in top_10.iterrows():
    organism = row['organism']
    drug = row['name']
    rate_r = row['rate_r']
    # add the number of experiment times 
    experiment_times = row['experiment_times']
    print('organism: ', organism, 'drug: ', drug, 'rate_r: ', rate_r, 'experiment_times: ', experiment_times)

# evaluate the mean of resistance rate of each organism 

# create a data frame for mean of resistance rate of each organism
mean_df = pd.DataFrame(columns=['organism', 'mean_rate_r'])
mean_df['organism'] = org

# calculate mean of resistance rate of each organism with the codition that both S and R are not zero
for o in org:
    mean_df.loc[mean_df['organism'] == o, 'mean_rate_r'] = count_df.loc[(count_df['organism'] == o) & (count_df['S'] != 0) & (count_df['R'] != 0), 'rate_r'].mean()

print('mean')
print(mean_df)

#calculate standard deviation of resistance rate of each organism with the codition that both S and R are not zero
for o in org:
    mean_df.loc[mean_df['organism'] == o, 'std_rate_r'] = count_df.loc[(count_df['organism'] == o) & (count_df['S'] != 0) & (count_df['R'] != 0), 'rate_r'].std()

print('std')
print(mean_df)

# plot bar graph of mean of resistance rate of each organism
plt.figure(figsize=(10, 10))
sns.barplot(x='mean_rate_r', y='organism', data=mean_df, palette='RdYlGn_r')
plt.xlabel('Mean of resistance rate')
plt.ylabel('Organism')
plt.title('Mean of resistance rate of each organism')
plt.grid()
# add label of each bar value
for index, value in enumerate(mean_df['mean_rate_r']):
    plt.text(value, index, str(round(value, 2)))

# move the grid to the back
plt.gca().set_axisbelow(True)
plt.show()
##########################################################################################################
# plot bar graph of mean of resistance rate of drug
# create a data frame for mean of resistance rate of each drug
mean_df = pd.DataFrame(columns=['drug', 'mean_rate_r'])
mean_df['drug'] = drug

