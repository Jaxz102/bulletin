from flask import Flask, redirect, url_for, render_template, request, session
import random
app = Flask(__name__)

# INDEX
@app.route("/") #HOME BUTTON PRESSED
def home():
    return render_template("index.html")

# LOGIN
@app.route("/login") #HOME BUTTON PRESSED
def loginFront():
    return render_template("login.html")

# ADMIN
@app.route("/admin", methods=['POST', 'GET']) #HOME BUTTON PRESSED
def admin():

    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "1234":
            return render_template("admin.html")
        else:
            return render_template("login.html", login_status = "False")

    return render_template("index.html", login_status = "True")

# ADD EVENTS
@app.route("/addevents") #HOME BUTTON PRESSED
def add():
    return render_template("add.html")


#pip3 install virtualenv
#virtualenv env
#source env/bin/activate
#pip3 install flask 



if __name__ == "__main__":
    app.run(debug=True)