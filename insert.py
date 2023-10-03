import psycopg2
conn = psycopg2.connect(user="postgres",
                 password="Kevin254!",
                 host="127.0.0.1",
                 port="5432",
                 database="myduka_class")
def insert_into_products(values):
    try:
        cursor = conn.cursor()
        columns="(product_name,buying_price,selling_price,stock_quantity)"
        values= "(%s, %s,%s, %s)"
        insert_query = f"INSERT INTO products{columns} {values}"
        # record_to_insert = values 

        cursor.execute(insert_query)

        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

values=('kiwi', 9000, 10000, 400)
pr = insert_into_products(values)
