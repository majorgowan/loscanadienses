def load_dataset():
    "Load the sample dataset."
    return [[apple, pear,orange], [grape, pear, kiwi], [apple, grape, pear, kiwi], [grape, kiwi]]
def createC1(dataset):
    "Create a list of candidate item sets of size one."
     c1 = []
        for transaction in dataset:
                for item in transaction:
                        if not [item] in c1:
                                c1.append([item])
                    c1.sort()
                 return map(frozenset, c1)
def createC1(dataset):
    "Create a list of candidate item sets of size one."
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
                c1.sort()
                return map(frozenset, c1)
cd /Users/KarenJung/Documents/loscanadienses
import Apriori.apriori as apriori
%paste
globals()
dataSet
ds
suppData
reload(apriori)
dataSet = ds
dataSet
L, suppData = apriori.apriori(dataSet,minSupport=0.5)
L
suppData
rules=apriori.generateRules(L,suppData,minConf=0.7)
ds
rules=apriori.generateRules(L,suppData,minConf=0.4)
import pandas as pd
sant_df = pd.read_csv('Data/train_ver2.csv')
sant_df.head()
sant_df.describe()
len(sant_df)
sant_df.columns
zip(range(len(sant_df.columns)),sant_df.columns)
baskets_df = sant_df.iloc[:10000,24:]
len(baskets_df)
baskets_df.head()
baskets_df.columns
ds
baskets_zeros = baskets_df.values.to_list()
baskets_zeros = baskets_df.values.tolist()
baskets_zeros[:10]
baskets_zeros[:2]
baskets_zeros[0]
cols = baskets_df.columns
cols
cols = list(baskets_df.columns)
cols
baskets_zeros[0]
baskets_names = []
for basket in baskets_names:
    c
baskets_names = []
for basket in baskets_zeros:
    b = [cols[i] for i,x in enumerate(basket) if x==1.0]
    baskets_names.append(b)
baskets_names[0]
baskets_names[:5]
baskets_names[:15]
baskets_names[:25]
import matplotlib.pyplot as plt
bsize = [len(basket) for basket in baskets_names]
bsize[:10]
plt.hist(bsize)
plt.show()
%history --help
%help(history)
%help %history
%help
help(%history)
%history
%?
%help
%%help
%history -f santander_columns_to_baskets.py
