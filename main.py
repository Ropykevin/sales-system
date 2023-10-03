import psycopg2
from flask import Flask, render_template, request, redirect
from dbservice import get_data

app = Flask(__name__)

# Establish a database connection
conn = psycopg2.connect(
    database="myduka_class",
    user="postgres",
    password="Kevin254!",
    host="localhost",
    port="5432"
)

# Route for the homepage
@app.route("/")
def sales_system():
    return render_template("index.html")

# Route for the dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Route for displaying and handling product data
@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "POST":
        cursor = conn.cursor()

        # Get form data
        product_name = request.form['product_name']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        stock_quantity = request.form['stock_quantity']

        # Using placeholders (%) instead of (?, ?, ?, ?) for PostgreSQL
        cursor.execute(
            "INSERT INTO products (product_name, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s)",
            (product_name, buying_price, selling_price, stock_quantity)
        )

        # Commit the changes to the database
        conn.commit()

        # Close the cursor
        cursor.close()

        # Redirect to the product listing page
        return redirect('/products')

    else:
        # If it's a GET request, fetch and display the product data
        products_data = get_data("products")
        return render_template("products.html", myproducts=products_data)

# Route for displaying and handling sales data
@app.route("/sales", methods=["GET", "POST"])
def sales():
    sales_data = get_data('sales')
    return render_template("sales.html", mysales=sales_data)

if __name__ == "__main__":
    app.run()
