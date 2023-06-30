from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)


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
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
