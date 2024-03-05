import snowflake.connector as sfc
from jproperties import Properties


def runQuery(conn, query, values):
    try:
        curs = conn.cursor()
        print(query, values)
        curs.execute(query, values)

        print(curs.fetchall())

    except Exception as e:
        print(e)

    finally:
        conn.close()
        print("Completed")


def connectSnowflake(configs):
    try:
        conn = sfc.connect(
            user=configs.get("USERNAME").data,
            password=configs.get("PASSWORD").data,
            account=configs.get("PID").data,
            warehouse=configs.get("WAREHOUSE").data,
            database=configs.get("DATABASE").data,
            schema=configs.get("SCHEMA").data,
            region=configs.get("REGION").data
        )
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

    # query = "CREATE TABLE EMPLOYEE (" \
    #            "ID VARCHAR(10)," \
    #            "NAME TEXT(50)," \
    #            "AGE NUMBER(3)" \
    #        ");"

    # query = "INSERT INTO EMPLOYEE(ID,NAME,AGE) VALUES(%s, %s, %s)"
    # values = [5, "Fedrick", "43"]

    # query = "UPDATE EMPLOYEE SET AGE=%s WHERE NAME=%s;"
    # values = [26, "Sam"]

    # query = "DELETE FROM EMPLOYEE WHERE ID=%s;"
    # values = ["2"]

    # query = "SELECT * FROM EMPLOYEE;"
    # values=[]

    query = "SELECT * FROM EMPLOYEE WHERE AGE>=%s;"
    values = [30]

    runQuery(conn, query, values)


if __name__ == "__main__":
    main()
