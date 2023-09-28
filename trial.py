import psycopg2
conn = psycopg2.connect(
database="myduka_class", user='postgres', password='Kevin254!', 
host='localhost', port= '5432')


# def get_remaining_stock():
#     quantity = [] 
#     try:
#             cursor = conn.cursor()
#             # Execute the SQL query
#             cursor.execute('SELECT * FROM remaining_stock')
#             remaining_stock = cursor.fetchall()

#             for i in remaining_stock:
#                 product = {}  # new dictionary for each product
#                 product['name'] = i[1]
#                 product['rem_stock'] = i[2]
#                 quantity.append(product)

#             return {'success': True, 'data': quantity}

#     except Exception as error:
#         # Handle exceptions, e.g., database connection error
#         error_message = str(error)
#         return {'success': False, 'error_message': error_message}

# # Example usage:
# result = get_remaining_stock()
# if result['success']:
#     stock_data = result['data']
#     for product in stock_data:
#         print(f"Product: {product['name']}, Remaining Stock: {product['rem_stock']}")
# else:
#     print(f"Error: {result['error_message']}")

def get_remaining_stock():
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT name, rem_stock FROM rem_stock')
        stock_data = [{'name': name, 'rem_stock': rem_stock} for name, rem_stock in cursor.fetchall()]
        return {'success': True, 'data': stock_data}
    except Exception as error:
        return {'success': False, 'error_message': str(error)}

# Example usage:
result = get_remaining_stock()
if result['success']:
    for product in result['data']:
        print(f"Product: {product['name']}, Remaining Stock: {product['rem_stock']}")
else:
    print(f"Error: {result['error_message']}")

