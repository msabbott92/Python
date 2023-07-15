from flask import render_template, request, redirect, session, flash
from wall_app import app
from flask_bcrypt import Bcrypt  
from wall_app.models.wall_model import User
from wall_app.models.post_model import Post

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect("/")
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    print(data)
    user = User.get_by_email(data)
    print(user)
    if not user:
        flash("Invalid Email!", "login")
        return redirect("/")
    print("Got this far")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password!", "login"), 
        return redirect('/')
    session['user_id'] = user.id
    return redirect("/wall")

@app.route("/wall")
def the_wall():
    data = {
        "id": session['user_id']
    }
    posts = Post.get_all_posts()
    print(posts)
    return render_template("wall.html", user = User.get_one_by_id(data), posts = posts)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


