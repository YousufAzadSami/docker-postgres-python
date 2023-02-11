import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres_user", 
   user='postgres_user', 
   password='postgres_pass', 
   host='localhost', 
   port= '5432'
)

#Creating a cursor object using the cursor() method
print('\n\nCreating a cursor object using the cursor() method\n\n')

cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

cursor.execute("SELECT * FROM quote")
print(cursor.fetchone())


#Closing the connection
conn.close()