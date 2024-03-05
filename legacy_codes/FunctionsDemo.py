def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

x = int(input("Enter a number: "))
print(isEven(x))
