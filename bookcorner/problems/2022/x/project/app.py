from cs50 import SQL
# import sqlite3

# from sqlalchemy import create_engine, select
# from sqlalchemy import Table, Column, MetaData
# from sqlalchemy.sql import text

from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session
# from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL('sqlite:///bookstore.db')
# db = sqlite3.connect('bookstore.db')

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():

    """Show portfolio of stocks"""
    user_id = session["user_id"]
    books_1 = db.execute("SELECT * FROM books WHERE id<6")
    books_2 = db.execute("SELECT * FROM books WHERE id>5")

    json_total = db.execute("SELECT COUNT (*) FROM cart WHERE user_id = ?", user_id)
    total = json_total[0]["COUNT (*)"]

    json = db.execute("SELECT username FROM users WHERE id=?", user_id)
    username = json[0]["username"]

    # return jsonify(total)

    return render_template("index.html", books_1=books_1, books_2=books_2, username=username, total=total)


@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():

    user_id = session["user_id"]

    # POST
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            book_json = db.execute("SELECT title FROM books WHERE id = ?", id)
            book = book_json[0]["title"]

            db.execute("INSERT INTO cart (items, item_id, user_id) VALUES (?,?,?)", book, id, user_id)
            return redirect("/")

    # GET
    books = db.execute("SELECT * FROM cart WHERE user_id = ?", user_id)

    json = db.execute("SELECT username FROM users WHERE id=?", user_id)
    username = json[0]["username"]

    json_total = db.execute("SELECT COUNT (*) FROM cart WHERE user_id = ?", user_id)
    total = json_total[0]["COUNT (*)"]

    # return jsonify(books)
    return render_template("cart.html", books=books, username=username, total=total)


@app.route("/login", methods=["GET", "POST"])
def login():

    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():

    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():

    """Register user"""

    # user ဆီကနေ GET or POST ခွဲခြားမယ်
    if request.method == "GET":
        # GET ဆိုရင် html page ပဲ ပြပေးမယ်
        return render_template("register.html")
    else:
        # POST ဆိုရင် user ရဲ့ name, pass, confirm pass တောင်းမယ်
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # valid ဖြစ်မဖြစ် အကုန်စစ်မယ်
        if not username:
            return apology("Enter Username!")

        if not password:
            return apology("Enter Password!")

        if password != confirmation:
            return apology("Password Not Match")

        # user password ကို လွယ်လွယ် ကြည့်မရအောင် hask fun ခေါ်
        hash = generate_password_hash(password)

        # ထပ်ထည့်လို့မရမရ စမ်းမယ်/ ထည့်ပြီးနာမည်ရှိမရှိစမ်းကြည့်မယ်
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash)
        # ရှိရင် ပယ်ဖျက်ပြီး မရကြောင်းပြော
        except:
            return apology("Username already exits")
        # user အသစ်ကို မှတ်ထားမယ်
        session["user_id"] = new_user
        return redirect("/")


@app.route("/remove", methods=["POST"])
@login_required
def remove():

    # တခါတည်း တိုက်ရိုက်ယူ remove button အတွက်မလို့
    remove = request.form.get("remove_id")

    user_id = session["user_id"]

    delete_json = db.execute(
        "SELECT MIN(id) FROM cart WHERE user_id =? AND item_id=?", user_id, remove)

    delete_id = delete_json[0]["MIN(id)"]
    db.execute("DELETE FROM cart WHERE id = ?", delete_id)

    # return jsonify(delete_id)
    return redirect("/cart")



@app.route("/description", methods=["POST"])
@login_required
def description():

    user_id = session["user_id"]

    id = request.form.get("id")
    book_json = db.execute("SELECT * FROM books WHERE id = ?", id)
    books_title = book_json[0]["title"]
    books_id = book_json[0]["id"]

    json = db.execute("SELECT username FROM users WHERE id=?", user_id)
    username = json[0]["username"]

    json_total = db.execute("SELECT COUNT (*) FROM cart WHERE user_id = ?", user_id)
    total = json_total[0]["COUNT (*)"]

    # return jsonify(books_title, books_id)
    return render_template("description.html", books_title=books_title, books_id=books_id, username=username, total=total)
