import psycopg2
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
    cursor.execute(insert_query, values)
    conn.commit()


def calculate_profit():
    cursor = conn.cursor()
    run_query = """SELECT DATE(created_at) AS mydate,
    SUM((selling_price - buying_price) * sales.quantity) AS profit 
    FROM sales 
    JOIN products ON products.product_id = sales.product_id 
    GROUP BY mydate 
    ORDER BY mydate;"""
    cursor.execute(run_query)
    list_records = cursor.fetchall()
    return (list_records)


def check_email_exists(email):
    cursor = conn.cursor()
    query = "SELECT EXISTS(SELECT 1 FROM users WHERE email = %s)"
    cursor.execute(query, (email))
    exists = cursor.fetchone()[0]
    return exists


def check_email_password_match(email, password):
    cursor = conn.cursor()
    query = "SELECT user_id FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    if result is not None:
        user_id = result[0]
        return user_id
    else:
        return None



def create_user(full_name, email, password):
    cursor = conn.cursor()
    insert_query = "INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (full_name, email, password))
    conn.commit()



