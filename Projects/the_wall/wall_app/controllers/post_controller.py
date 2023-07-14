from flask import render_template, request, redirect, session, flash
from wall_app import app
from flask_bcrypt import Bcrypt  
from wall_app.models.wall_model import User
from wall_app.models.post_model import Post

@app.route("/posts", methods=['POST'])
def new_post():
    data = {
        "content" : request.form["content"],
        "users_id": session["user_id"]
    }
    print(data)
    Post.save(data)
    print("getting this far")

    return redirect('/wall')


