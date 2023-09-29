import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="myduka_class", user='postgres', password='Kevin254!', 
   host='localhost', port= '5432'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select * from products")

#Fetch a single row using fetchone() method.
data = cursor.fetchall()
print("Connection established to: ",data)

#Closing the connection
conn.close()
conn = psycopg2.connect(
database="myduka_class", user='postgres', password='Kevin254!', 
host='localhost', port= '5432')
# FUNTCTION
def get_data(table_name):
   cursor = conn.cursor()
   cursor.execute(f"select * from  {table_name}")
   list_of_records=cursor.fetchall()
   return list_of_records
    
products=get_data("products")
print(products)

sales=get_data("sales")
print(sales)

#  ONE TABLE
def insert_data_to_table(product_name, buying_price, selling_price, stock_quantity):
    try:
        
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO products (product_name, buying_price, selling_price, stock_quantity)
            VALUES (%s, %s, %s, %s)
        """
        record_to_insert = (product_name, buying_price,selling_price, stock_quantity)

        cursor.execute(insert_query, record_to_insert)
        conn.commit()
        print("Record inserted successfully")

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data:", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

insert_data_to_table('cute', 9000.0, 10000.0, 400)

   # multible table

def insert_into(table_name, values, columns):
    try:
        cursor = conn.cursor()
        placeholders = ', '.join(['%s'] * len(values))
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        cursor.execute(insert_query, values)
        conn.commit()
        print(f"Data inserted into {table_name} successfully")
    except (Exception, psycopg2.Error) as error:
        print(f"Failed to insert record into {table_name}: {error}")
    finally:
        if conn:
            conn.close()

values = ('soda', 500, 700, 100)
columns = ('product_name', 'buying_price', 'selling_price', 'stock_quantity')

insert_into('products', values, columns)
conn.close()


def remaining_stock():
    cursor = conn.cursor()
    # Query to fetch the remaining stock for each product
    cursor.execute("update products set stock_quantity=50")
    cursor.execute("SELECT product_name, stock_quantity FROM products")
    cursor.execute("SELECT sale_quantity, product_id FROM sales")

    # Fetch all rows and create a dictionary with product_name as key and remaining stock as value
    product_stock_dict = {product_name: stock_quantity for product_name, stock_quantity in cursor.fetchall()}
    sales_quantity_dict= {product_id: sale_quantity for product_id,sale_quantity in cursor.fetchall}
    remaining_stock_dict=product_stock_dict-sales_quantity_dict

    # Close the database connection
    conn.close()

    return remaining_stock_dict

