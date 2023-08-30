#!/usr/bin/env python
from flask import Flask, render_template, session, request, url_for, redirect
from datetime import timedelta
import sqlite3
from functions import *

app = Flask(__name__)
app.secret_key = "a6sidg7fo8hyug2irhyug7hd8owiundilfaud"

#AS
conn = sqlite3.connect('/data/user.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT NOT NULL,
                   password TEXT NOT NULL,
                   image TEXT NOT NULL DEFAULT "image.png",
                   name TEXT NOT NULL DEFAULT "",
                   quote TEXT NOT NULL DEFAULT "",
                   submission INTEGER DEFAULT "0"
               )''')
conn.commit()

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("email")
        password = request.form.get("password")
        #if user info isnt in databse add it otherwise log in
        if check_if_user_exists(username): # chheck if user email is in datdabase
            if authenticate_user(username, password): # if both user and pass exist
                session["logged_in"] = True
                session["email"] = username
                return redirect(url_for('home'))
            else:
                x = ":D"
                return render_template("login.html", incorrect = x)
        else:
            add_user(username, password) #user cannot be found creating new data entry
            session["email"] = username
            session["logged_in"] = True
            return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if 'logged_in' in session and session['logged_in']:#if logged in present the following
        user_email = session["email"]
        has_entered = get_status(user_email)
        if request.method == "POST":
            name = request.form.get("name") #UDC
            quote = request.form.get("quote") #UDC
            email = session["email"]  #UDC
            if name and quote and email: # if all udc criteria are met
                update_name_quote(name, quote, email) # update database with data
                user_data = get_all_user_data() # collect all data to pass to jinja
                #has_submitted(email) # tell sql user has submitted
                return render_template("index.html", user_data = user_data)
        user_data = get_all_user_data() # passing fata to jinja
        return render_template("index.html", user_data = user_data, stat=has_entered)
    else:
        return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

