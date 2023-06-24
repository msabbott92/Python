from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def level_one():
    return render_template("index.html")

@app.route("/play/<int:num>/<string:color>")
def level_two(num, color):
    return render_template("level2.html", num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)