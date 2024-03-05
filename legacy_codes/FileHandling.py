try:
    fin = open("resources/newEmps.txt", "r")
    fout = open("resources/Employees.txt", "a")
    items = fin.readlines()
    print(items)
    fout.write("\n")
    for eachLine in items:
        print(eachLine, end="")
        fout.write(eachLine)
except FileNotFoundError as e:
    print(e)
finally:
    fin.close()
    fout.close()
