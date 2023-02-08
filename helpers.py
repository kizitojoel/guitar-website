import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

def apology(message, code=400):
    def remove_special(s):
        for special, new in [(" ", "-"), ("-", "--"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(special, new)
        return s
    return render_template("apology.html", top=code, bottom=remove_special(message)), code

def login_required(f):
    @wraps(f)
    def decorate_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorate_function