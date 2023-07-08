from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("index.html", users=User.get_all())

@app.route('/create')
def new_user():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def new_create():
    if not User.validate_user(request.form):
        return redirect("/create")
    print(request.form)
    User.save(request.form)
    return redirect("/")

@app.route("/users/<int:id>")
def show_dojo(id):
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

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username": request.form['username'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/dashboard")