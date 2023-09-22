import psycopg2
# #establishing the connection
# conn = psycopg2.connect(
#    database="myduka_class", user='postgres', password='Kevin254!', 
#    host='localhost', port= '5432'
# )

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Executing an MYSQL function using the execute() method
# cursor.execute("select * from products")

# #Fetch a single row using fetchone() method.
# data = cursor.fetchall()
# print("Connection established to: ",data)

# #Closing the connection
# conn.close()
conn = psycopg2.connect(
database="myduka_class", user='postgres', password='Kevin254!', 
host='localhost', port= '5432')
# FUNTCTION
def get_data(b):
   cursor = conn.cursor()
   cursor.execute(f"select * from  {b}")
   list_of_records=cursor.fetchall()
   return list_of_records
    
prods=get_data("products")
print(prods)

sales=get_data("sales")
print(sales)