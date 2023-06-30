from flask import Flask, render_template, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

from friend import Friend
@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    #data = {
    #    "fname": request.form["fname"],
    #    "lname": request.form["lname"],
    #    "occ": request.form["occ"]
    #}
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    friend=Friend.get_one(friend_id)
    return render_template("show_friend.html", friend=friend)    

if __name__ == "__main__":
    app.run(debug=True)

