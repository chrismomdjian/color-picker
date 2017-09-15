from flask import Flask, render_template, url_for, redirect
from data import colors

app = Flask(__name__)

@app.route("/home/<string:color>", methods=["GET"])
def home(color):
    choices = [choice for choice in colors]
    return render_template("home.html", color=color, choices=choices)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
