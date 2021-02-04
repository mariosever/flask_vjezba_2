from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    poruka = "Ovo je poruka iz python programa!"

    return render_template("index.html", poruka=poruka)


@app.route("/onama")
def onama():

    ucenici = ["Ivo", "Ana", "Marko"]

    return render_template("onama.html", ucenici=ucenici)

@app.route("/proizvodi")
def proizvodi():

    proizvodi = ["Monitor", "Miš", "Tipkovnica"]

    return render_template("proizvodi.html", proizvodi=proizvodi)


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


if __name__ == "__main__":
    app.run()
