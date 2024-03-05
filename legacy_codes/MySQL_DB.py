import mysql.connector as db

#id, name, age, city = input("Enter id, name, age and city: ").split(",")

try:
    myDB = db.connect(host="", port="", user="", passwd="")
    myCursor = myDB.cursor()

    '''insertQuery = "INSERT INTO crm_demo.customers(id, name, age, city) VALUES (%s, %s, %s, %s)"
    vals = (int(id), name, int(age), city)
    myCursor.execute(insertQuery, vals)
    myDB.commit()

    if myCursor.rowcount == 1:
        print("Record inserted successfully!!!")'''

    selectQuery = "SELECT * FROM crm_demo.customers WHERE age>30 ORDER BY name"
    myCursor.execute(selectQuery)

    res = myCursor.fetchall()

    for eachRecord in res:
        print(eachRecord)

    myDB.close()
except Exception as e:
    print(e)
finally:
    print("Completed")
