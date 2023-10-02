import psycopg2
from flask import Flask,render_template,request, redirect
from dbservice import get_data,insert_sales,insert_products
app=Flask(__name__)
conn = psycopg2.connect(
database="myduka_class", user='postgres', password='Kevin254!', 
host='localhost', port= '5432')

@app.route("/")
def sales_system():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/products", methods=["GET", "POST"])
def products():
    products =get_data("products")
    insert_data=insert_products(conn)
    return render_template("products.html",myproducts=products,products_insert=insert_data)

@app.route("/sales", methods=["GET", "POST"])
def sales():
    sales_data = get_data('sales') 
    insert_sale=insert_sales(conn)

    return render_template("sales.html", mysales=sales_data,sales_insert=insert_sale)



app.run()
