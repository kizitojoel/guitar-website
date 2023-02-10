from flask import Flask
import os
from cs50 import SQL
from flask import Flask, flash, render_template, request, session, redirect
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import login_required, apology


#Configure application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Configure session to use filesystem(instead of sign cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# CS50 Library to use SQLite
db = SQL("sqlite:///guitar.db")

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
    return render_template("index.html")

# Route for the register, including SQL support for storing usernames and passwords
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("password-confirm")

        # Check if the passwords match each other
        if password != confirm:
            return apology("Passwords don't match")

        # Check if username is already taken
        existingUsers = db.execute("SELECT * FROM users WHERE username = ?;", username)
        if existingUsers:
            return apology("Username already taken")

        #Add the username to the database and the password hash
        password_hash = generate_password_hash(password)
        db.execute("INSERT INTO users(username, hash) VALUES (?, ?);", username, password_hash)

        #Alert registration successful and redirect to the login page
        flash("You have been successfully registered", "info")
        return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log our guitar user in"""

    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        #Check if the password matches the password hash
        # If yes, log the user in and redirect them to the homepage
        rows = db.execute("SELECT * FROM users WHERE username = ?;", username)
        print(rows)

        #Check if there is such a user
        print("This thing works")
        if len(rows) != 1:
            print("No user")
            return apology("No such user exists")
            

        password_hash = rows[0]["hash"]
        if check_password_hash(password_hash, password):
            session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/lesson1", methods=["GET"])
def lesson():
    return render_template("lesson1.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

