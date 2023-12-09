from flask import Flask, render_template

from database import select_last

app = Flask(__name__)


@app.route("/")
def main_page():
    people = select_last()
    return render_template("index.html", people=people)
