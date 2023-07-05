from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.models.d_j_model import Dojo, Ninja

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

@app.route("/ninjas")
def new_ninja():
    return render_template("ninja.html", dojos = Dojo.get_all())

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
    }
    print(data)
    
    return redirect("/dojos")






