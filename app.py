from flask import Flask, redirect, url_for, render_template, request, session
import random
app = Flask(__name__)

# ["Name", "Datetime", "Location", "Description", "Link", "Tags"]

events = [
    ["Community BBQ", "Datetime", "Address", "Description", "Link", "Tags"],
    ["Bicycle Festival", "Datetime", "Address", "Description", "Link", "Tags"],
    ["Community Swimming", "Datetime", "Address", "Description", "Link", "Tags"],
    ["Art Gallery Exhibit", "Datetime", "Address", "Description", "Link", "Tags"]
]
proposed = [
    ["Community Lunch", "Datetime", "Location", "Description", "Link", "Tags"],
    ["Community Church Session", "Datetime", "Location", "Description", "Link", "Tags"]
]

# Sorting algo
def sort(lst, sorttype):

    if sorttype == "alpha1":
        index = 0
        order = "ascending"
    elif sorttype == "alpha2":
        index = 0
        order = "descending"

    lower = []
    equal = []
    larger = []

    if len(lst) != 0 and order == "ascending":
        pivot = lst[0]
        for i in lst:
            if i[index] < pivot[index]:
                lower.append(i)
            elif i[index] == pivot[index]:
                equal.append(i)
            else:
                larger.append(i)
        return sort(lower, sorttype) + equal + sort(larger, sorttype)
    elif len(lst) != 0 and order == "descending":
        pivot = lst[0]
        for i in lst:
            if i[index] > pivot[index]:
                lower.append(i)
            elif i[index] == pivot[index]:
                equal.append(i)
            else:
                larger.append(i)
        return sort(lower, sorttype) + equal + sort(larger, sorttype)
    else:
        return lst



# INDEX
@app.route("/") #HOME BUTTON PRESSED
def home():
    return render_template("index.html", eventsdb = events)
# Waiting for datetime algo
# @app.route("/date1")
# def date1():
#     return render_template("index.html", eventsdb = sort(events, "date1"))
# @app.route("/date2")
# def date2():
#     return render_template("index.html", eventsdb = sort(events, "date2"))
@app.route("/alpha1")
def alpha1():
    return render_template("index.html", eventsdb = sort(events, "alpha1"))
@app.route("/alpha2")
def alpha2():
    return render_template("index.html", eventsdb = sort(events, "alpha2"))




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