# make sure to be in the home loscanadienses folder
# cd /Users/KarenJung/Documents/loscanadienses
# cd /home/mfruman/DataSci/loscanadienses

# pandas for dataframes
import pandas as pd
# numpy for various
import numpy as np
# matplotlib for plotting
import matplotlib.pyplot as plt

# apriori algorithm (for support and confidence rules)
# code from 
#
#    Harrington, Peter "Machine Learning in Action" (Manning)
#
import Apriori.apriori as apriori

# for manipulating Santander data and applying apriori
# algorithm
import Santander.baskets as sbaskets

# load Santander training data as pandas dataframe
sant_df = pd.read_csv('Data/train_ver2.csv')

### Train association rules
# randomly sample batches of rows, generate association rules,
# and average the generated rules by grouping by (left-hand-side,right-hand-side) pair
min_supp = 0.02
min_conf = 0.25
rule_batches = []
nbatches = 20
batchsize = 10000
seed = 666
# random state (to set seed for repeatable training)
ran_state = np.random.RandomState(seed)
for i in xrange(nbatches):
    print('Training with batch number ... %d' % i)
    sample_df = sant_df.sample(n=batchsize,random_state=ran_state)
    # convert batch of customer data into "baskets" of financial products
    sb = sbaskets.makeBaskets(sample_df,(0,batchsize),(24,48),withNcodpers=False)
    # find all sets of products that occur in at least min_supp of the baskets
    Ls, supp = apriori.apriori(sb,minSupport=min_supp)
    # find all rules that have confidence at least min_conf
    # (i.e. a rule A=>B is a pair of subsets A and B such that B occurs in
    # at least a fraction minConf of the baskets in which A occurs)
    rule_batches.append(apriori.generateRules(Ls,supp,minConf=min_conf))
# flatten list of rules into list of pairs of form ((ls,rs),conf), 
# where ls and rs are *sorted* lists of left-hand-sides and right-hand-sides
# of the rules
rules = [((sorted(list(rule[0])),sorted(list(rule[1]))),rule[2]) for rules in rule_batches for rule in rules]
# loop over rules and average confidence of each rule
rules_unique = []
confs_average = []
for rule in rules:
    if rule[0] in rules_unique:
        confs_average[rules_unique.index(rule[0])] += rule[1]
    else:
        rules_unique.append(rule[0])
        confs_average.append(rule[1])
confs_average = [conf/nbatches for conf in confs_average]
rules_average = [(frozenset(b[0]),frozenset(b[1]),a) for (a,b) in sorted(zip(confs_average,rules_unique),reverse=True)]

### Apply rules to customers based on their baskets in current month
# generate list of unique customers
customers = sbaskets.customers(sant_df)
# months of data to use for prediction
curr_date = '2016-04-28'
pred_date = '2016-05-28'
# group by month
sant_by_month_grps = sant_df.groupby('fecha_dato')
# dataframes of only single months
curr = sant_by_month_grps.get_group(curr_date)
actual = sant_by_month_grps.get_group(pred_date)
# generate customer baskets for current month
curr_baskets = sbaskets.makeBaskets(curr)
# apply rules to each basket
preds = sbaskets.allSuggestions(rules_average, curr_baskets)


#################### TO DO
- compare predictions to actual baskets
- tune hyperparameters (min_supp, min_conf, threshhold_conf)
- cluster on other columns (use random samples to compute cluster centres)
- repeat association rules separately for each customer cluster
- apply to test set and submit ASAP!!!

