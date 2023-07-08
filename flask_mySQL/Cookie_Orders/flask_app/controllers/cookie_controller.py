from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.cookie_model import Cookie

@app.route("/cookies")
def cookie_orders():
    cookies = Cookie.get_all()
    print(cookies)
    return render_template("index.html", cookies = cookies)

@app.route("/cookies/new")
def new_cookie():
    return render_template('new_order.html')

@app.route("/cookies/order", methods=['POST'])
def new_order():
    if not Cookie.validate_cookie(request.form):
        return redirect('/cookies/new')
    Cookie.save(request.form)
    return redirect('/cookies')

@app.route("/edit/<int:id>")
def edit_order_page(id):
    data = {"id": id}
    return render_template("edit.html", cookie = Cookie.get_one(data))

@app.route("/update/<int:id>", methods = ["POST"])
def update_order(id):
    if not Cookie.validate_cookie(request.form):
        return redirect(f'/edit/{id}')
    Cookie.update(request.form)
    return redirect("/cookies")

    

