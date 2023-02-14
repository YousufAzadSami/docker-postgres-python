import logging
import psycopg2
import time
import datetime as dt

print('\nManually waiting 5s (via time.sleep()) for the Postgres to start. Not the best solution, but it will do for now.\n')
time.sleep(5)


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

def select_all():
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

def delete_older_dates(date_threshold = dt.date(2023, 2, 23)):
    print(f'\nDeleting records that are older than {date_threshold}')
    sql_query = "DELETE FROM customers where (customer_date < %s);"
    # print(sql_query)
    cursor.execute(sql_query, (date_threshold, ))
    conn.commit()

def select_condition():
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

def connection_related_stuff():
    pass

if __name__ == '__main__':

    select_all()

    # select_condition()

    delete_older_dates()

    select_all()
    

    #Closing the connection
    conn.close()
