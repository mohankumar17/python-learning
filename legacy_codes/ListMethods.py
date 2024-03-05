from functools import reduce

items = [i for i in range(2, 14, 3)]
print(items)

odds = list(filter((lambda n : n%2 != 0),items))
print(odds)

triples = list(map((lambda n : n * 3),odds))
print(triples)

sum_triples = reduce((lambda n,acc=0 : n + acc),triples)
print(sum_triples)

prod_items = reduce((lambda n,acc=1 : n * acc),items)
print(prod_items)