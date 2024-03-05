#a, b = map(int, input("Enter two nums: ").split())
#items = [12, 13, 14, 15]

try:
    print(int(input("Enter a number: ")))
    #print("a/b: ", (a // b))
    #print(items[21])
except(IndexError):
    print("Index out of bounds")
except ZeroDivisionError as e:
    print("Can't be divided by Zero, Msg:", e)
except Exception as e:
    print("Global Exception Handler, Msg:", e)
finally:
    print("Process Completed")
