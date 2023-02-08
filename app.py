from flask import Flask
import os
from cs50 import SQL
from flask import Flask, flash, render_template, request, session, redirect
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import login_required


#Configure application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Configure session to use filesystem(insted of sign cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# CS50 Library to use SQLite
db = SQL("sqlite:///guitar.db")


@app.route("/")
@login_required
def hello():
    return "Hello World"


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log our guitar user in"""

    session.clear()

    return render_template("login.html")
