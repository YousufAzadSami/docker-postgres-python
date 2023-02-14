import psycopg2
import time
import datetime as dt


def select_all(cursor):
    print(f'Selecting and printing all rows from the table "customers" - \n')
    sql_query = f"SELECT * FROM customers;"
    # print(sql_query)
    cursor.execute(sql_query)
    sql_rows = cursor.fetchall()
    print_rows(sql_rows)

    print(f'Row count: {cursor.rowcount}\n')

def print_rows(rows):
    for row in rows:
        print(row)

def delete_older_dates(cursor, date_threshold = dt.date(2023, 2, 23)):
    print(f'Deleting records that are older than {date_threshold}\n')
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

def wait_a_while():
    for x in range(5):
        print(f'Waiting manually for 5 seconds so that the Postgres container can start first : {5-x}s left') 
        time.sleep(1)
    print('Waited manually (via time.sleep()) for 5 seconds so that the Postgres container can start first. Not the best solution, but it will do for now\n')

if __name__ == '__main__':

    # waiting a while so that the Postgres container can start first
    wait_a_while()

    # for the sake of simplicity, I am putting the whole connection and sql query part in the inside of try
    try:
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
        cursor.execute('SELECT version()')
        print(f'Connection established to {cursor.fetchone()}')
        print(f'\nThe Postgres container is preloaded with a "customers" table in the "postgres_super_db" database from customers.sql file. It has 5 records\n')

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
    
    except:
        print('Something went wrong. Following the print statements will give us a clue')
