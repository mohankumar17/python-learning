import intrest_rate_module as irm

print(irm.categories)

rate = irm.getIntrestRate("B")
print(f"Intrest Rate: {rate}")

siOb = irm.SimpleIntrest(rate=rate)
simple_intrest = siOb.getSimpleIntrest(amount=100000, tenure=3)

print(f"Simple Intrest: {simple_intrest}")

################################################

from intrest_rate_module import categories, SimpleIntrest, getIntrestRate

print(categories)

rate = getIntrestRate("A")
print(f"Intrest Rate: {rate}")

siOb = SimpleIntrest(rate=rate)
simple_intrest = siOb.getSimpleIntrest(amount=200000, tenure=5)

print(f"Simple Intrest: {simple_intrest}")
