from flask import Flask, redirect, url_for, render_template, request, session
import datetime 
import random
app = Flask(__name__)

# ["Name", "Datetime", "Location", "Description", "Link", "Tags"]
events = [
    ["Community BBQ", datetime.datetime(2021, 5, 3, 9, 30), "1718 Eglinton Avenue, Toronto", "Join us on May 3rd for our 25th annual community BBQ!", "https://www.eworldtrade.com/events/beach-bbq-amp-brews-festival/", "#bbq #barbecue #food"],
    ["Bicycle Festival", datetime.datetime(2021, 5, 10, 12, 00), "2454 Craven Place, Medicine Hat", "On May 10, 2021, join the excitement of BikeRide’s giveaway contests! Each month you can win innovative and practical bike accessories. You could even win a brand new bicycle.", "https://www.bikeride.com/giveaways/", "#bike #bicycle #fitness #getactive"],
    ["Community Swimming", datetime.datetime(2021, 6, 7, 6, 00), "279 Central Pkwy, Malton", "Welcome to Splash Works, our 20-acre premier water park where families can splish, splash and laugh! Splash Works features 17 different water slides and water attractions that are sure to please thrillseekers big and small. ", "https://www.canadaswonderland.com/splash-works", "#swimming #pool #cooldown"],
    ["Art Gallery Exhibit", datetime.datetime(2021, 5, 2, 9, 15), "14 Elm St 3RD floor, Toronto", "The Ontario Society of Artists (OSA) welcomes Canadian artists to apply to participate in our 148th Annual Open Juried Exhibition of Fine Arts on May 2, 2021. Details of the event will be provided to the artists at the notification date.", "https://ontariosocietyofartists.org/osa-148th-annual-open-juried-art-exhibition/", "#art #gallery"]
]
proposed = [
    ["Community Church Session", datetime.datetime(2021, 6, 3, 9, 30), "Location", "Description", "Link", "#church #god #unity"],
    ["Community Lunch", datetime.datetime(2021, 6, 3, 11, 30), "Location", "Description", "Link", "#lunch #yum #food"]
]

def date_str(lst):

    dates = []
    for event in lst:
        dates.append(event[1].strftime('%m/%d/%Y %H:%M'))
    return dates

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
    return render_template("index.html", eventsdb = sort(events, "date1"), datelst = date_str(sort(events, "date1")), lstlen=len(sort(events, "date1")))
# SORTING MENU
@app.route("/date1")
def date1():
    return render_template("index.html", eventsdb = sort(events, "date1"), datelst = date_str(sort(events, "date1")), lstlen=len(sort(events, "date1")))
@app.route("/date2")
def date2():
    return render_template("index.html", eventsdb = sort(events, "date2"), datelst = date_str(sort(events, "date2")), lstlen=len(sort(events, "alpha1")))
@app.route("/alpha1")
def alpha1():
    return render_template("index.html", eventsdb = sort(events, "alpha1"), datelst = date_str(sort(events, "alpha1")), lstlen=len(sort(events, "alpha1")))
@app.route("/alpha2")
def alpha2():
    return render_template("index.html", eventsdb = sort(events, "alpha2"), datelst = date_str(sort(events, "alpha2")), lstlen=len(sort(events, "alpha2")))

# LOGIN
@app.route("/login") #HOME BUTTON PRESSED
def loginFront():
    return render_template("login.html")

# ADMIN
@app.route("/admin", methods=['POST', 'GET']) #HOME BUTTON PRESSED
def admin():

    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "1234":
            return render_template("admin.html", proposedevents = proposed)
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
        address = request.form.get("address") + " ," + request.form.get("city")
        link = request.form.get("link")
        tags = request.form.get("tags")
        description = request.form.get("description")

        proposed.append([name, date, address, description, link, tags])
        print(proposed)
        return render_template("index.html", eventsdb = sort(events, "date1"), datelst = date_str(sort(events, "date1")), lstlen=len(sort(events, "date1")))



@app.route("/adminedit", methods = ["POST"])
def edit():
    if request.method == "POST":
        status = request.form["status"]
        name = request.form["name"]
        print(name)

        if(status == "accept"):
            for i in reversed(range(len(proposed))):
                if proposed[i][0] == name:
                    events.append(proposed[i])
                    del proposed[i]
        elif(status == "reject"):
            for i in reversed(range(len(proposed))):
                if proposed[i][0] == name:
                    del proposed[i]

    return render_template("admin.html", proposedevents = proposed)


if __name__ == "__main__":
    app.run(debug=True)


    
