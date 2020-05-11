from flask import Flask, render_template, request, redirect, url_for, \
    make_response  # import vom Modul flask der klasse "flask"
import random
import datetime
from models import User, db

from werkzeug.utils import redirect

app = Flask(__name__)  # instance von der "flask" klasse
db.create_all()


@app.route("/")  # "/" ist home folder --> der pfad
def main():
    return render_template("main.html")


@app.route("/e1-facebook")
def fakebook():
    return render_template("e1-facebook.html")


@app.route("/friseursalon")
def friseursalon():
    return render_template("/friseursalon.html")


@app.route("/boogle")
def boogle():
    return render_template("/boogle.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/lucky_number", methods=['GET', 'POST'])
def lucky_number():
    if request.method == "GET":
        secret_number = request.cookies.get("lucky_number/secret")
        if not secret_number:
            secret_number = random.randint(1, 10)

        context = {
            "date_of_number": datetime.datetime.now().isoformat(),
        }

        response = make_response(render_template("lucky_number.html", **context))  # 2.tes Argument ist context)
        response.set_cookie("lucky_number/secret", str(secret_number))

        return response

    elif request.method == "POST":
        user_guess = request.form.get('number')
        user_secret_cookie = request.cookies.get("lucky_number/secret")
        if user_guess == user_secret_cookie:
            print("User succeeded in guessing")

            response = make_response(redirect(url_for('lucky_number_success')))
            response.set_cookie("lucky_number/secret", expires=0)
            return response
        else:
            print("user guessed wrong: ", user_guess, " but secret number was: ", user_secret_cookie)
            return redirect(url_for('lucky_number'))


@app.route("/lucky_number/success", methods=["GET"])
def lucky_number_success():
    return render_template("lucky_number_success.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        users = db.query(User).all()
        context = {
            "users": users
        }
        return render_template("register.html", **context )
    elif request.method == "POST":
        username = request.form.get("username")
        new_user = User(name=username, secret_number=10)
        db.add(new_user)    # wie git add --> speichert vor commit
        db.commit()         # git commit --> abspeichern aller geaddeten elemente in einer transaktion.
        return redirect(url_for('register'))


# TODO: 1) add boogle site
# TODO: 2) add hair dresser site


if __name__ == '__main__':
    app.run(debug=True)  # ist eine dauerschleife
