x, y = map(int, input("Enter X and Y: ").split())

for i in range(x, 0, -1):
    for j in range(0, i):
        print("#", end=" ")
    print()
