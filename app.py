from flask import Flask, redirect, url_for, render_template, request, session
import datetime 
import random
app = Flask(__name__)

# ["Name", "Datetime", "Location", "Description", "Link", "Tags"]
events = [
    ["Community BBQ", datetime.datetime(2021, 5, 3, 9, 30), "Address", "Join us on May 3rd for our 25th annual community BBQ!", "Link", "#bbq #barbecue #food"],
    ["Bicycle Festival", datetime.datetime(2021, 5, 10, 12, 00), "Address", "Description", "Link", "#bike #bicycle #fitness #getactive"],
    ["Community Swimming", datetime.datetime(2021, 6, 7, 6, 00), "Address", "Description", "Link", "#swimming #pool #cooldown"],
    ["Art Gallery Exhibit", datetime.datetime(2021, 5, 2, 9, 15), "Address", "Description", "Link", "#art #gallery"]
]
proposed = [
    ["Community Lunch", "Datetime", "Location", "Description", "Link", "Tags"],
    ["Community Church Session", "Datetime", "Location", "Description", "Link", "Tags"]
]

# Sorting algo
def sort(lst, sorttype):

    lower = []
    equal = []
    larger = []

    if len(lst) != 0 and sorttype == "date1":
        pivot = lst[0]
        for i in lst:
            if i[1] < pivot[1]:
                lower.append(i)
            elif i[1] == pivot[1]:
                equal.append(i)
            else:
                larger.append(i)
        return sort(lower, sorttype) + equal + sort(larger, sorttype)
    if len(lst) != 0 and sorttype == "date2":
        pivot = lst[0]
        for i in lst:
            if i[1] > pivot[1]:
                lower.append(i)
            elif i[1] == pivot[1]:
                equal.append(i)
            else:
                larger.append(i)
        return sort(lower, sorttype) + equal + sort(larger, sorttype)
    if len(lst) != 0 and sorttype == "alpha1":
        pivot = lst[0]
        for i in lst:
            if i[0] < pivot[0]:
                lower.append(i)
            elif i[0] == pivot[0]:
                equal.append(i)
            else:
                larger.append(i)
        return sort(lower, sorttype) + equal + sort(larger, sorttype)
    elif len(lst) != 0 and sorttype == "alpha2":
        pivot = lst[0]
        for i in lst:
            if i[0] > pivot[0]:
                lower.append(i)
            elif i[0] == pivot[0]:
                equal.append(i)
            else:
                larger.append(i)
        return sort(lower, sorttype) + equal + sort(larger, sorttype)
    else:
        return lst



# INDEX
@app.route("/") #HOME BUTTON PRESSED
def home():
    return render_template("index.html", eventsdb = sort(events, "date1"))
# SORTING MENU
@app.route("/date1")
def date1():
    return render_template("index.html", eventsdb = sort(events, "date1"))
@app.route("/date2")
def date2():
    return render_template("index.html", eventsdb = sort(events, "date2"))
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

# ADDING EVENTS
@app.route("/adding", methods = ["POST"])
def adding():
    if request.method == "POST":
        name = request.form.get("name")
        date = datetime.datetime(*[int(v) for v in request.form.get("date").replace('T', '-').replace(':', '-').split('-')])
        address = request.form.get("address") + request.form.get("city")
        link = request.form.get("link")
        tags = request.form.get("tags")
        description = request.form.get("description")

        # events.append([name, date, address, description, link, tags])
        proposed.append([name, date, address, description, link, tags])
        return render_template("index.html", eventsdb = sort(events, "date1"))

if __name__ == "__main__":
    app.run(debug=True)