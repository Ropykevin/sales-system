import psycopg2
from flask import request, redirect


conn = psycopg2.connect(
database="myduka_class", user='postgres', password='Kevin254!', 
host='localhost', port= '5432')

def get_data(table_name):
   cursor = conn.cursor()
   cursor.execute(f"select * from  {table_name}")
   list_of_records=cursor.fetchall()
   return list_of_records

def insert_products(conn):
    try:
        cursor = conn.cursor()
        product_name = request.form["product_name"]
        buying_price = request.form["buying_price"]
        selling_price = request.form["selling_price"]
        stock_quantity = request.form["stock_quantity"]
        insert_query = "INSERT INTO products (product_name, buying_price,selling_price,stock_quantity) VALUES (%s, %s,%s, %s)"
        cursor.execute(insert_query, (product_name,buying_price,selling_price,stock_quantity))
        conn.commit()
        return redirect("/products")
    except (Exception, psycopg2.Error) as error:
        conn.rollback()
        return f"Failed to insert record: {error}"
    finally:
        if cursor:
            cursor.close()
def insert_sales(conn):
    try:
        cursor = conn.cursor()
        product_id = request.form["product_id"]
        quantity = request.form["quantity"]
        created_at = request.form["created_at"]
        insert_query = "INSERT INTO sales (product_id, quantity,created_at) VALUES (%s, %s,%s)"
        cursor.execute(insert_query, (product_id,quantity,created_at))
        conn.commit()
        return redirect("/sales")
    except (Exception, psycopg2.Error) as error:
        conn.rollback()
        return f"Failed to insert record: {error}"
    finally:
        if cursor:
            cursor.close()
            


# def insert_data(table_name, values, columns):
#     try:
#         cursor = conn.cursor()
#         placeholders = ', '.join(['%s'] * len(values))
#         insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
#         cursor.execute(insert_query, values)
#         conn.commit()
#         print(f"Data inserted into {table_name} successfully")
#     except (Exception, psycopg2.Error) as error:
#         print(f"Failed to insert record into {table_name}: {error}")
#     finally:
#         if conn:
#             conn.close()
#             import psycopg2

