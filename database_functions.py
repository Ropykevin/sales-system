import psycopg2

conn = psycopg2.connect(
database="myduka_class", user='postgres', password='Kevin254!', 
host='localhost', port= '5432')

def table_details(table_name):
   cursor = conn.cursor()
   cursor.execute(f"select * from  {table_name}")
   list_of_records=cursor.fetchall()
   return list_of_records

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