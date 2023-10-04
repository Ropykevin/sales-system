import psycopg2
from flask import request, redirect

conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='Kevin254!',
    host='localhost', port='5432')

def get_data(table_name):
    cursor = conn.cursor()
    cursor.execute(f"select * from {table_name}")
    list_of_records = cursor.fetchall()
    return list_of_records

def insert_products(values):
    cursor = conn.cursor()
    insert_query = "INSERT INTO products (product_name, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, values)
    conn.commit()

def insert_sale(values):
    cursor = conn.cursor()
    insert_query = "INSERT INTO sales (product_id, quantity, created_at) VALUES (%s,%s, now())"
    cursor.execute(insert_query,values)
    conn.commit()
