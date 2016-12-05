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
baskets_names[:10]
ds
Ls, supp = apriori.apriori(baskets_names,minSupport=0.1)
Ls
Ls, supp = apriori.apriori(baskets_names,minSupport=0.01)
Ls
supp
rules_sant=apriori.generateRules(Ls,supp,minConf=0.01)
rules_sant=apriori.generateRules(Ls,supp,minConf=0.05)
rules_sant=apriori.generateRules(Ls,supp,minConf=0.25)
ls
cp /Users/KarenJung/Downloads/sample_submission.csv Data
head Data/sample_submission.csv
len(cols)
cols
import Santander.baskets as baskets
import Santander.baskets as sbaskets
sb = sbaskets(sant_df,[0,10000],[24,48])
sb = sbaskets.makeBaskets(sant_df,[0,10000],[24,48])
sb[:10]
sant_df.columns
customers = sorted(list(set(sant_df.ncodpers)))
customers[:10]
len(customers)
1.0*len(sant_df)/len(customers)
sant_df.iloc[:12,:5]
sant_df[ncodpers==1375586].iloc[:12,:5]
sant_df[sant_df[ncodpers]==1375586].iloc[:,:5]
sant_df[sant_df['ncodpers']==1375586].iloc[:,:5]
reload(sbaskets)
sb = sbaskets.makeBaskets(sant_df,[0,10000],[24,48])
sb[:10]
%%timeit
sb = sbaskets.makeBaskets(sant_df,[0,10000],[24,48])
%%time
sb = sbaskets.makeBaskets(sant_df,[0,10000],[24,48])
%%time
sb = sbaskets.makeBaskets(sant_df,[0,100000],[24,48])
%%time
sb = sbaskets.makeBaskets(sant_df,[0,1000000],[24,48])
%%time
sb = sbaskets.makeBaskets(sant_df,[0,1000000],[24,48],withNcodpers=False)
sb[:10]
plt.hist([len(basket) for basket in sb])
plt.show()
plt.hist([len(basket) for basket in sb],bins=range(24))
plt.show()
rules_sant
[rule[0] for rule in rules]
[rule[0] for rule in sant_rules]
[rule[0] for rule in rules_sant]
sb[10]
sb[100]
sb[:20]
sb[:30]
xxx = [1, 2, 3, 4]
xxxset = set(xxx)
xxxset.issubset(xxxset)
set([1,2,3])
set([1,2,3]).issubset(xxxset)
reload(sbaskets)
sb[:10]
rules_sant
sbaskets.applyRules(rules_sant,sb[0])
allsug = [sbaskets.applyRules(rules_sant,basket) for basket in sb[:1000]]
allsug[:30]
sb[21]
sant_df.iloc[21,'ncodpers']
sant_df.iat[21,'ncodpers']
sant_df.at[21,'ncodpers']
sant_df[sant_df.ncodpers==1050586].iloc[:,24:48]
rules_sant
rules_sant=apriori.generateRules(Ls,supp,minConf=0.25)
ds
rules_sant=apriori.generateRules(Ls,supp,minConf=0.25)
Ls, supp = apriori.apriori(sb,minSupport=0.01)
len(Ls)
Ls
supp
rules_sant=apriori.generateRules(Ls,supp,minConf=0.25)
len(rules_sant)
allsug = [sbaskets.applyRules(rules_sant,basket) for basket in sb[:1000]]
allsug[:40]
[sug for sug in allsug if len(sug)>0]
reload(sbaskets)
allsug = [sbaskets.applyRules(rules_sant,basket) for basket in sb[:1000]]
[sug for sug in allsug if len(sug)>0]
reload(sbaskets)
sbaskets.makeBaskets(sbaskets.customerData(sant_df,1375586))
sbaskets.customerData(sant_df,1375586)
reload(sbaskets)
sbaskets.customerData(sant_df,1375586)
customers[:10]
for customer in customers:
    pass
for customer in customers[:10]:
    sbaskets.customerData(sant_df,customer)
for customer in customers[:10]:
    print sbaskets.customerData(sant_df,customer)
for customer in customers[:1]:
    print sbaskets.customerData(sant_df,customer)
sbaskets.customerData(sant_df,customers[0])
sbaskets.customerData(sant_df,customers[0],withNcodpers=False)
reload(sbaskets)
sbaskets.customerData(sant_df,customers[0],withNcodpers=False)
sant_df.columns
reload(sbaskets)
sbaskets.onlyMonth(sant_df,dateString='2016-04-28',customers[:10])
sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:10])
sant_df.columns
sant_df.dtypes
sant_df[0]
sant_df.loc[0,:]
reload(sbaskets)
reload(sbaskets)
sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:10])
reload(sbaskets)
sant_df.loc[0,'fecha_dato']
sbaskets.customerData(sant_df,customers[0],withNcodpers=False)
sbaskets.customerData(sant_df,customers[0])
sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:10])
reload(sbaskets)
sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:10])
april = sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:10])
may = sbaskets.onlyMonth(sant_df,'2016-05-28',customers[:10])
zip(april,may)
%history -f santander_history_day0.py
