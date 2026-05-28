from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
import sqlite3
app = Flask(__name__)
app.secret_key = "secretkey"
bcrypt = Bcrypt(app)
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")
conn.commit()
@app.route("/")
def home():
    if "user" in session:
        return render_template("home.html", user=session["user"])
    return redirect("/login")
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
        return redirect("/login")
    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )
        user = cursor.fetchone()
        if user:
            stored_password = user[2]
            if bcrypt.check_password_hash(stored_password, password):
                session["user"] = username
                return redirect("/")
        return "Invalid Username or Password"
    return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")
if __name__ == "__main__":
    app.run()
