from flask import Flask,render_template
from dbservice import get_data,insert_data
app=Flask(__name__)


@app.route("/")
def sales_system():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/products")
def products():
    products =get_data("products")
    return render_template("products.html",myproducts=products)

@app.route("/sales")
def sales():
    sales=get_data("sales")
    return render_template("sales.html",mysales=sales)
app.run()