from flask import Flask, render_template, request, redirect, session,flash, url_for
from dbservice import get_data, insert_products, insert_sale, calculate_profit, create_user, check_email_password_match,check_email_exists

app = Flask(__name__)
app.secret_key = "Kevin254!"


# def login_check():
#     if session['email']!=None:
#         return redirect(url_for("dashboard"))
# Route for the homepage
@app.route("/")
def sales_system():
    return render_template("index.html")

# Route for the dashboard


@app.route("/dashboard")
def dashboard():
    # login_check()
    if "user_id" not in session:
        return redirect("/login")
    dates = []
    profits = []
    for i in calculate_profit():
        dates.append(str(i[0]))
        profits.append(float(i[1]))
    return render_template("dashboard.html", dates=dates, profits=profits)


# Route for displaying and handling product data
@app.route("/add-product", methods=["POST"])
def add_products():
    product_name = request.form['product_name']
    buying_price = request.form['buying_price']
    selling_price = request.form['selling_price']
    stock_quantity = request.form['stock_quantity']
    columns = (product_name, buying_price, selling_price, stock_quantity)
    insert_products(columns)
    return redirect('/products')


@app.route("/products")
def products():
    # login_check()

    if "user_id" not in session:
        return redirect("/login")
    products_data = get_data("products")
    return render_template("products.html", myproducts=products_data)

# Route for displaying and handling sales data


@app.route("/sales", methods=["GET", "POST"])
def sales():
    # login_check()

    if "user_id" not in session:
        return redirect("/login")
    sales_data = get_data('sales')
    products = get_data("products")
    return render_template("sales.html", mysales=sales_data, products=products)


@app.route("/add-sales", methods=["POST"])
def add_sales():
    product_id = request.form["product_id"]
    quantity = request.form['quantity']
    msale = (product_id, quantity)
    insert_sale(msale)

    return redirect('/sales')


@app.route("/register", methods=["POST","GET"])
def register():
    full_name = request.form["full_name"]
    email = request.form["email"]
    password = request.form["pass"]
    create_user(full_name, email, password)

    if not check_email_exists(email):
        create_user(full_name, email, password)
        return redirect('/login')
    else:
        flash ("Email already exists.")
        return redirect('/login')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user_id=check_email_password_match(email, password)

        if user_id:
            session["user_id"] = user_id
            return redirect('/dashboard')
        else:
            flash ("Login failed. Please check your email and password.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
