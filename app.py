from flask import Flask, redirect, url_for, render_template, request, session
import random
app = Flask(__name__)

# INDEX
@app.route("/") #HOME BUTTON PRESSED
def home():
    return render_template("index.html")

#pip3 install virtualenv
#virtualenv env
#source env/bin/activate
#pip3 install flask 



if __name__ == "__main__":
    app.run(debug=True)