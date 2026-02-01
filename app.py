from flask import Flask, request, Response, render_template
from connectsheet import init_csv, add_expense, read_expenses
from storeexcel import init_users_csv, store_data

app = Flask(__name__)

# Initialize CSV files at startup
init_csv()
init_users_csv()

# ✅ Store expenses in CSV file
@app.route("/store_expense", methods=["POST"])
def save_expense():
    data = request.json
    add_expense(data["date"], data["method"], data["amount"])
    return "Expense Saved", 200

# ✅ Fetch expenses from CSV file
@app.route("/show", methods=["GET"])
def show_csv():
    expenses = read_expenses()
    if not expenses:
        return "No expenses recorded yet!", 404
    # Return plain text view of CSV data
    return Response("\n".join([",".join(row) for row in expenses]), content_type="text/plain")

# ✅ Signup route (stores user data in users.csv)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        if not name or not password:
            return "Error: Name and password fields are required!", 400
        store_data(name, password)
        return "Signup Successful!"
    return render_template("demo.html")

# ✅ Other pages
@app.route("/start")
def start():
    return render_template("start.html") 

@app.route("/category")
def category():
    return render_template("category.html")

@app.route("/accounts")
def accounts():
    return render_template("accounts.html")

@app.route("/currency")
def currency():
    return render_template("currency.html")

@app.route("/dis")
def dis_page():
    return render_template("dis.html")

if __name__ == "__main__":
    app.run(debug=True)
