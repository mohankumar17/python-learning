import pyodbc
from jproperties import Properties


def runQuery(conn, query, values):
    try:
        curs = conn.cursor()
        print(query %values)
        curs.execute(query %values)

        #print(curs.fetchall())
        for eachRow in curs.fetchall():
            print(eachRow)

        curs.close()
    except Exception as e:
        print(e)

    finally:
        conn.close()
        print("Completed")
def connectSnowflake(configs):
    try:
        host = configs.get("HOST").data
        port = configs.get("PORT").data
        accountid = configs.get("ACCOUNTID").data
        roleid = configs.get("ROLEID").data
        username = configs.get("USERNAME").data
        password = configs.get("PASSWORD").data

        conn = pyodbc.connect(
            'DRIVER=NetSuite Drivers 64bit;Host=' + host + ';Port=' + port + ';Encrypted=1;AllowSinglePacketLogout=1;Truststore=system;SDSN=NetSuite.com; UID=' + username + ';PWD=' + password + ';CustomProperties=AccountID=' + accountid + ';RoleID=' + roleid)
        return conn
    except ConnectionError as ex:
        print(ex)
        return -1


def main():
    configs = Properties()
    with open('dev.properties', 'rb') as config_file:
        configs.load(config_file)

    conn = connectSnowflake(configs)
    if conn == -1:
        print("Connection Error")
    else:
      print("Connection Successful!!")

      #query = 'SELECT TRANSACTION_ID FROM TRANSACTIONS;'
      #query = 'SELECT account_id, accountnumber, full_name, openbalance, date_last_modified FROM ACCOUNTS ORDER BY account_id;'
      query = 'SELECT account_id, accountnumber, full_name, openbalance, date_last_modified FROM ACCOUNTS WHERE account_id<=%s ORDER BY openbalance DESC;'

      values = 10
      runQuery(conn, query, values)


if __name__ == "__main__":
    main()
