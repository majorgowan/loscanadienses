def makeBaskets(df, rows = None, cols = (24,48), withNcodpers=True):
    if rows is None:
        rows = (0,len(df))
    baskets_df = df.iloc[rows[0]:rows[1],cols[0]:cols[1]]
    baskets_zeros = baskets_df.values.tolist()
    cols = list(baskets_df.columns)
    baskets_names = []
    for basket in baskets_zeros:
        b = [cols[i] for i,x in enumerate(basket) if x==1.0]
        baskets_names.append(b)
    if withNcodpers:
        ncodpers = df.ncodpers[rows[0]:rows[1]]
        fecha_dato = df.fecha_dato[rows[0]:rows[1]]
        return zip(ncodpers,fecha_dato,baskets_names)
    else:
        return baskets_names

def compareBaskets(basket1, basket2):
    # given two baskets, find products in *second* basket that are not in first
    return sorted(list(set(basket2).difference(set(basket1))))

def applyRules(rules, basket):
    leftsides = [rule[0] for rule in rules]
    rightsides = [rule[1] for rule in rules]
    confs = [rule[2] for rule in rules]
    bset = set(basket)
    suggestions = []
    for i,leftside in enumerate(leftsides):
        if (leftside.issubset(bset)):
            for item in rightsides[i]:
                if item not in basket:
                    suggestions.append((item,confs[i]))
    return suggestions

def maxSet(prods_with_confs):
    # given a list of pairs of non-unique products with confidences
    # return a list of unique products with the maximum confidence of each
    # sorted by maximum confidence
    #
    # sort by increasing confidence
    return_list = sorted(prods_with_confs,key=lambda a: a[1])
    # convert to dictionary (cheat, keeps only last value for each key)
    return_dict = dict(return_list)
    # convert back to list
    return_list = [(key,return_dict[key]) for key in return_dict]
    # sort by decreasing confidence
    return sorted(return_list,key=lambda a: -a[1])

def allSuggestions(rules, customerBaskets, withConfs=True):
    allsug = []
    for cb in customerBaskets:
        cust_id = cb[0]
        basket = cb[2]
        if (len(basket) > 0):
            # keep only maximum-confidence rule for each suggestions
            suggestions = maxSet(applyRules(rules,basket))
            if withConfs:
                allsug.append((cust_id,suggestions))
            else:
                allsug.append((cust_id,[a[0] for a in suggestions]))
        else:
            allsug.append((cust_id,[]))
    return allsug

def allAdditions(old_baskets, new_baskets):
    # given lists of old and new baskets, of the form
    #   [(ncodpers, {??,} ['item1','item2', ...]]
    # where {??,} represents an optional date string
    # find all items in each new_basket that were not in
    # corresponding old_basket
    #
    # (if date_string present, strip it)
    new_dict = dict([(a[0],a[-1]) for a in new_baskets])
    old_dict = dict([(a[0],a[-1]) for a in old_baskets])
    additions = []
    for cust_id in new_dict:
        if cust_id not in old_dict:
            additions.append((cust_id, new_dict[cust_id]))
        else:
            additions.append((cust_id, compareBaskets(old_dict[cust_id],new_dict[cust_id])))
    return sorted(additions)

def evaluateBasket(pred_basket, ref_basket):
    # compute the average precision @ 7 
    total_prec = 0.0
    ncorrect = 0.0
    if len(ref_basket) == 0:
        return 0.0
    for i,item in enumerate(pred_basket[:7]):
        if item in ref_basket:
            ncorrect += 1.0
            total_prec += ncorrect/(i+1.0)
    return total_prec / min(7,len(ref_basket))

def wayOfAllFlesh(curr_baskets, pred_baskets, popularity, cutoff=7):
    # given lists of current and predicted baskets in form of (cust_id, basket) pairs 
    # and a list of most popular products (product, frequency)
    # fill in values up to cutoff with most popular products not already in basket or suggestions
    products = [a[0] for a in popularity]
    filled_baskets = []
    curr_dict = dict([(a[0],a[-1]) for a in curr_baskets])
    for basket in pred_baskets:
        if basket[0] in curr_dict:
            bask = basket[1] + \
                    [prod for prod in products \
                        if prod not in (curr_dict[basket[0]] + basket[1])]
        else:
            bask = basket[1] + [prod for prod in products if prod not in basket[1]]
        filled_baskets.append((basket[0],bask[:cutoff]))
    return filled_baskets        

def evaluateAll(pred_baskets, curr_baskets, actual_baskets):
    additions = allAdditions(curr_baskets, actual_baskets)
    additions_dict = dict([(a[0],a[-1]) for a in additions])
    pred_dict = dict([(a[0],a[-1]) for a in pred_baskets])
    scores = []
    for cust_id in additions_dict:
        if cust_id in pred_dict:
            scores.append((cust_id, \
                           additions_dict[cust_id], \
                           pred_dict[cust_id], \
                           evaluateBasket(pred_dict[cust_id],additions_dict[cust_id])))
    total_score = sum(score[-1] for score in scores) / len(scores)
    print('total score: ' + str(total_score))
    return scores

def customers(df, idfield = 'ncodpers'):
    return sorted(list(set(df[idfield])))

def customerData(df, id, idfield = 'ncodpers', withNcodpers=True):
    return makeBaskets(df[df[idfield]==id],withNcodpers=withNcodpers)

def makeSubmissionCSV(baskets, filename='submission_file.csv'):
    with open(filename,'w') as outfile:
        outfile.write('ncodpers,added_products\n')
        for basket in baskets:
            outfile.write(str(basket[0]) + ',' + ' '.join([p for p in basket[-1]]) + '\n')
