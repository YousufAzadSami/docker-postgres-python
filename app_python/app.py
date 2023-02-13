import logging
import psycopg2
import time
import datetime as dt



if __name__ == '__main__':

    print('\nWaiting for the Postgres to start\n')
    # time.sleep(5)

    #establishing the connection
    conn = psycopg2.connect(
        database="postgres_super_db", 
        user='postgres_user', 
        password='postgres_pass', 
        host='localhost', 
        port= '5432'
    )

    #Creating a cursor object using the cursor() method
    print('\nCreating a cursor object using the cursor() method')

    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute("select version()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print(f"\nConnection established to: {data}\n")

    date_limit = '2023-02-23'
    date_2 = dt.date(2023, 2, 23)
    # # sql_query = f"SELECT * FROM customers where customer_date<'{date_limit}'"
    # sql_query = f"DELETE FROM customers where customer_date<'{date_limit}'"
    # print(sql_query)
    # cursor.execute(sql_query)
    # conn.commit()
    # sql_query = f"SELECT FROM customers where customer_date<'{date_limit}'"

    sql_query = f"SELECT * FROM customers;"
    print(sql_query)
    cursor.execute(sql_query)
    print(cursor.fetchall())

    print(f'\nRow count: {cursor.rowcount}\n')

    # sql_query = f"SELECT * FROM customers"
    sql_query = "SELECT * FROM customers where customer_id < 3;"
    print(sql_query)
    cursor.execute(sql_query)
    print(cursor.fetchall())
    # print(type(cursor.fetchall()))

    sql_query = "SELECT * FROM customers where customer_id < %s;"
    print(sql_query)
    cursor.execute(sql_query, (3, ))
    print(cursor.fetchall())

    sql_query = "SELECT * FROM customers where customer_date < %s;"
    print(sql_query)
    cursor.execute(sql_query, (date_2, ))
    print(cursor.fetchall())

    sql_query = "DELETE FROM customers where customer_date < %s;"
    print(sql_query)
    cursor.execute(sql_query, (date_2, ))
    # print(cursor.fetchall())
    conn.commit()

    sql_query = f"SELECT * FROM customers;"
    print(sql_query)
    cursor.execute(sql_query)
    print(cursor.fetchall())
    

    #Closing the connection
    conn.close()
