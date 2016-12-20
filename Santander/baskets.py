def makeBaskets(df, rows = (0,10000), cols = (24,48), withNcodpers=True):
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

def allSuggestions(rules, customerBaskets):
    allsug = []
    for cb in customerBaskets:
        cust_id = cb[0]
        basket = cb[1]
        if (len(basket) > 0):
            # print basket[0], len(basket[0])
            allsug.append((cust_id,applyRules(rules,basket[0])))
        else:
            allsug.append((cust_id,[]))
    return allsug

def customers(df, idfield = 'ncodpers'):
    return sorted(list(set(df[idfield])))

def customerData(df, id, idfield = 'ncodpers', withNcodpers=True):
    return makeBaskets(df[df[idfield]==id],withNcodpers=withNcodpers)

def onlyMonth(df, dateString, customers):
    month_df = df[df['fecha_dato']==dateString]
    baskets = []
    for customer in customers:
        baskets.append((customer, \
                       makeBaskets(month_df[month_df['ncodpers']==customer], \
                                   withNcodpers=False)))
        # print 'customer ' + str(customer)
    return baskets
