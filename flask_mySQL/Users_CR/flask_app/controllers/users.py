from flask_app import app
from flask import Flask, render_template, request, redirect, session
from models.user import User


@app.route("/")
def index():
    return render_template("index.html", users=User.get_all())

@app.route('/create')
def new_user():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def new_create():
    print(request.form)
    User.save(request.form)
    return redirect("/")

@app.route("/users/<int:id>")
def show_user(id):
    data = {
        "id": id
    }
    return render_template("user.html", user=User.get_one(data))

@app.route("/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def destroy(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/')