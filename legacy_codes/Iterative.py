items = input("Enter items in the list: ").split(" ")

ind = 0
while ind < len(items):
    items[ind] = int(items[ind])
    ind += 1

for eachInd in range(0, len(items)):
    if items[eachInd] % 2 == 0:
        continue
    items[eachInd] *= 2

print(items)

for eachItem in items:
    if eachItem % 5 == 0:
        break
    print(eachItem, end=" ")
print()

