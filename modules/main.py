#import tax_module as tax
from tax_module import Tax, getTotalAmount

#taxOb = tax.Tax(rate=18)
#print(taxOb.getTaxAmount(amount=10000))
#print(tax.getTotalAmount(rate=15, amount=20000))

taxOb = Tax(rate=18)
print(taxOb.getTaxAmount(amount=10000))
print(getTotalAmount(rate=15, amount=20000))