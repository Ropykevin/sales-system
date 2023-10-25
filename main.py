from flask import Flask, render_template, request, redirect, session, url_for, flash
from dbservice import get_data, insert_products, insert_sale, calculate_profit, create_user, check_email_password_match, check_email_exists

app = Flask(__name__)
app.secret_key = "Kevin254!"


@app.route("/")
def sales_system():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    dates = []
    profits = []
    for i in calculate_profit():
        dates.append(str(i[0]))
        profits.append(float(i[1]))
    return render_template("dashboard.html", dates=dates, profits=profits)


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
    if "user_id" not in session:
        return redirect("/login")
    products_data = get_data("products")
    return render_template("products.html", myproducts=products_data)


@app.route("/sales", methods=["GET", "POST"])
def sales():
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


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        password = request.form["pass"]

        if not check_email_exists(email):
            create_user(full_name, email, password)
            flash("acount created successfuly","success")
            return redirect('/login')
        else:
            flash("Email already exists. Please use a different email.", "error")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = check_email_password_match(email, password)
        
        if user:
            user_id, full_name = user 
            session['user_id'] = user_id
            session['user_name'] = full_name
            flash(f'Welcome, {full_name}')
            return redirect(url_for("dashboard"))  

        elif not check_email_exists(email):
            flash("Email not found. Please register.")
            return redirect(url_for("register"))

        else:
            flash("Invalid login credentials. Please try again.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    if "user_id" in session:
        user_id = session["user_id"]
        user_name = session["user_name"]  

        flash(f"You have been logged out, {user_name}!")
        session.pop("user_id", None)
        session.pop("user_name", None)  

    return redirect(url_for('login')) 


if __name__ == "__main__":
    app.run(debug=True)
