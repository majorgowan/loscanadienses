import pandas
import pandas as pd
import Apriori.apriori as apriori
pwd
cd /Users/KarenJung/Documents/loscanadienses
import Apriori.apriori as apriori
import Santander.baskets as sbaskets
sant_df = pd.read_csv('Data/train_ver2.csv')
customers = sbaskets.customers(sant_df)
april = sbaskets.onlyMonth(sant_df,'2016-04-28',customers)
april = sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:10])
reload(sbaskets)
april = sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:10])
april = sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:1000])
reload(sbaskets)
april = sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:1000])
%%time
sb = sbaskets.makeBaskets(sant_df,[0,1000000],[24,48])
Ls, supp = apriori.apriori(sb,minSupport=0.01)
%%time
sb = sbaskets.makeBaskets(sant_df,[0,100000],[24,48])
%%time
Ls, supp = apriori.apriori(sb,minSupport=0.01)
%%time
sb = sbaskets.makeBaskets(sant_df,[0,10000],[24,48])
%%time
Ls, supp = apriori.apriori(sb,minSupport=0.05)
sb[:10]
%%time
Ls, supp = apriori.apriori(sb,minSupport=0.05,withNcodpers=False)
help(sbaskets.makeBaskets)
%%time
sb = sbaskets.makeBaskets(sant_df,[0,10000],[24,48],withNcodpers=False)
%%time
Ls, supp = apriori.apriori(sb,minSupport=0.05)
%%time
sb = sbaskets.makeBaskets(sant_df,[0,100000],[24,48],withNcodpers=False)
%%time
Ls, supp = apriori.apriori(sb,minSupport=0.05)
Ls
%%time
Ls, supp = apriori.apriori(sb,minSupport=0.01)
Ls
%%time
Ls, supp = apriori.apriori(sb,minSupport=0.02)
Ls
supp
%%time
rules_sant = apriori.generateRules(Ls,supp,minConf=0.25)
rules_sant
april[:10]
sb[0]
reload(sbaskets)
april = sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:1000])
reload(sbaskets)
april = sbaskets.onlyMonth(sant_df,'2016-04-28',customers[:1000])
allsug = [sbaskets.applyRules(rules_sant,basket) for basket in [x[1][0] for x in april]]]
allsug = [sbaskets.applyRules(rules_sant,basket) for basket in [x[1][0] for x in april]]
april[0]
[x[1][0] for x in april[:2]]
sb[:2]
allsug = [sbaskets.applyRules(rules_sant,basket) for basket in [x[1][0] for x in april]]
allsug = [sbaskets.applyRules(rules_sant,basket) for basket in sb[:1000]]
sb[:20]
april[:10]
[x[1][0] for x in april[:2]]
allsug = [basket for basket in sb[:1000]]
allsug
allsug[:2]
allsug = [basket for basket in [x[1][0] for x in april]]
allsug = [basket for basket in [x[1][0] for x in april[:10]]]
allsug = [basket for basket in [x[1][0] for x in april[:1]]]
allsug = [basket for basket in [x[1][0] for x in april[:2]]]
april[:10]
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april)
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april)
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april[:10])
april[:3]
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april[:10])
len([])
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april[:10])
[].isempty()
[].is_empty()
[].isEmpty()
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april[:10])
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april[:10])
allsug = sbaskets.allSuggestions(rules_sant, april[:10])
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april[:10])
april[2]
april[3]
reload(sbaskets)
allsug = sbaskets.allSuggestions(rules_sant, april[:10])
allsug
rules
rules_sant
allsug
sant_df[sant_df['ncodpers']==15897]
%history -f History/santander_history_day1.py
