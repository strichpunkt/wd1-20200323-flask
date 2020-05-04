from flask import Flask     # import vom Modul flask der klasse "flask"

app = Flask(__name__)       # instance von der "flask" klasse


@app.route("/")             # "/" ist home folder --> der pfad
def index():
    return "Hello, SmartNinja!"


if __name__ == '__main__':
    app.run()               # ist eine dauerschleife
