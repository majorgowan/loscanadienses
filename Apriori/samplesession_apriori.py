cd Apriori
import apriori

# find all subsets of the full item set that occur in at least half the baskets
ds = apriori.loadDataSet()
L,suppData=apriori.apriori(ds, 0.5)
L
suppData

# ... in at least three quarters of the baskets
L,suppData=apriori.apriori(ds,0.75)
L
suppData
