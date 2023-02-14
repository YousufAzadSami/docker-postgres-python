import psycopg2
import time
import datetime as dt


def select_all(cursor):
    print(f'\nSelecting and printing all rows from the table "customers"\n')
    sql_query = f"SELECT * FROM customers;"
    # print(sql_query)
    cursor.execute(sql_query)
    sql_rows = cursor.fetchall()
    print_rows(sql_rows)

    print(f'\nRow count: {cursor.rowcount}\n')

def print_rows(rows):
    for row in rows:
        print(row)

def delete_older_dates(cursor, date_threshold = dt.date(2023, 2, 23)):
    print(f'\nDeleting records that are older than {date_threshold}')
    sql_query = "DELETE FROM customers where (customer_date < %s);"
    # print(sql_query)
    cursor.execute(sql_query, (date_threshold, ))
    conn.commit()

def select_condition(cursor):
    date_2 = dt.date(2023, 2, 23)
    sql_query = "SELECT * FROM customers where customer_id < 3;"
    print(sql_query)
    cursor.execute(sql_query)
    sql_rows = cursor.fetchall()
    print_rows(sql_rows)

    sql_query = "SELECT * FROM customers where customer_id < %s;"
    print(sql_query)
    cursor.execute(sql_query, (3, ))
    print_rows(sql_rows)

    sql_query = "SELECT * FROM customers where (customer_date < %s);"
    print(sql_query)
    cursor.execute(sql_query, (date_2, ))
    print_rows(sql_rows)

if __name__ == '__main__':

    print('\nManually waiting 5s (via time.sleep()) for the Postgres container to start. Not the best solution, but it will do for now.\n')
    for x in range(5):
        print(f'Waiting for 5 seconds : {5-x}s left') 
        time.sleep(1)

    #establishing the connection
    conn = psycopg2.connect(
        database="postgres_super_db", 
        user='postgres_user', 
        password='postgres_pass', 
        host='db', 
        port= '5432'
    )
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # select and print everything from the 'customer' table in the database
    select_all(cursor)

    # select and print some stuff depending on the condition from the 'customer' table in the database
    # select_condition(cursor)

    # delete all the records that are older than a certain date
    delete_older_dates(cursor)
    # or
    # delete_older_dates(cursor, dt.date(2023, 2, 24))

    # select and print everything from the 'customer' table in the database
    select_all(cursor)
    

    #Closing the connection
    print('closing the connection')
    conn.close()
