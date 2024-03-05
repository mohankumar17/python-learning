x = int(input("Enter a number: "))

if x % 3 == 0 and x % 5 != 0:
    print("Divisible by 3 only")
elif x % 3 != 0 and x % 5 == 0:
    print("Divisible by 5 only")
elif x % 3 == 0 and x % 5 == 0:
    print("Divisible by both 5 and 3")
else:
    print("Not divisible by 5 and 3")
