import psycopg2

def insert_into_table(table, values):
    try:
        conn = psycopg2.connect(user="postgres",
                                      password="Kevin254!",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="myduka_class")
        cursor = conn.cursor()

        insert_query = f"INSERT INTO {table} VALUES (%s, %s, %s, %s)"
        record_to_insert = values 

        cursor.execute(insert_query, record_to_insert)

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

pr = insert_into_table("sales", ('kiwi', 9000, 10000, 400))
