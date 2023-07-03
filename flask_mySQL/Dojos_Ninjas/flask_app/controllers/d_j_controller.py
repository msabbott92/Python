from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.models.d_j_model import Dojo

@app.route("/dojos")
def index():
    return render_template("index.html", dojos = Dojo.get_all())

@app.route("/new_dojo", methods=["POST"])
def new_dojo():
    data = {
        "name": request.form["name"]
    }
    session['name'] = request.form["name"]
    print(data)
    Dojo.save(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show_user(id):
    data = {
        "id": id
    }
    return render_template("dojos.html", dojo = Dojo.get_one(data))

#You've linked the list of dojos to showing page, now link ninja data to the DB and then have it displayed. 





