from flask import Flask, render_template, request, redirect, url_for  # import vom Modul flask der klasse "flask"
import random
import datetime

from werkzeug.utils import redirect

app = Flask(__name__)       # instance von der "flask" klasse


@app.route("/")             # "/" ist home folder --> der pfad
def main():
    return render_template("main.html")


@app.route("/fakebook")
def fakebook():
    return render_template("e1-facebook.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/lucky_number", methods=['GET', 'POST'])
def lucky_number():

    if request.method=="GET":
        context = {
            "date_of_number": datetime.datetime.now().isoformat(),
            "lucky_number": random.randint(1, 10)
        }

        return render_template("lucky_number.html", **context)   # 2.tes Argument ist context

    elif request.method=="POST":
        return redirect(url_for('lucky_number'))

# TODO: 1) add boogle site
# TODO: 2) add hair dresser site


if __name__ == '__main__':
    app.run(debug=True)               # ist eine dauerschleife
