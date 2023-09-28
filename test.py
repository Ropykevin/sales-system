from database_functions import insert_into

values = (20, 500,'now')
columns = ('product_id','quantity','created_at')

insert_into('sales', values, columns)

values = ('soda', 500, 700, 100)
columns = ('product_name', 'buying_price', 'selling_price', 'stock_quantity')

insert_into('products', values, columns)