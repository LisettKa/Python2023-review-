from flask import Flask, render_template

from database import DBAccessor

app = Flask(__name__)


@app.route("/")
def main_page():
    people = DBAccessor().select_last()
    return render_template("index.html", people=people)
