from crypt import methods
from webbrowser import get
from app import app
from flask import render_template


from models.shop import *


@app.route("/")
def index():
    return "Hello World!"


@app.route("/orders")
def get_orders():
    return render_template("index.html", title="Home", orders=orders)


@app.route("/orders/<index>")
def get_order_details(index):
    return render_template(
        "order.html", title="Order details", order=orders[int(index)]
    )
