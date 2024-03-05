import snowflake.connector as sfc
from jproperties import Properties
from snowflake.connector.pandas_tools import write_pandas
import pandas
def runQuery(conn, query, values):
    try:
        curs = conn.cursor()
        print(query)
        curs.execute(query, values)

        #success, nchunks, nrows, _ = write_pandas(conn, values, 'EMPLOYEE')
        #print(success, nchunks, nrows)

        #print(curs.fetchall())
        df = curs.fetch_pandas_all()
        print(df)

        #df = curs.fetch_pandas_batches()
        #for eachRow in df:
        #    print(eachRow["NAME"])

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

    query = "SELECT * FROM EMPLOYEE;"
    values = []

    #query = "SELECT * FROM EMPLOYEE WHERE AGE>=%s;"
    #values = [30]

    #query = ""
    #values = pandas.DataFrame([(6, 'Mark', 35), (7, 'Luke', 24)], columns=['ID', 'NAME', 'AGE'])

    runQuery(conn, query, values)


if __name__ == "__main__":
    main()
