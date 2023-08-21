from flask import Flask, render_template, request

from fukcijos import parodyk_ora, temp_val

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"]) ###########################
def login():
    if request.method == "GET":
        return render_template("forma.html")
    if request.method == "POST":
        vardas = request.form["laukelis"]
        return render_template("vardas.html", sablono_kint=vardas)


    # ############ kitas aprasymo variantas
    # if request.method == "POST":
    #     vardas = request.form["laukelis"]
    #     return render_template("vardas.html", sablono_kint=vardas)
    # else:
    #     return render_template("forma.html")



@app.route("/orai")
def orai():
    oraskk = parodyk_ora("Vilnius", 1)
    tempval = temp_val("Vilnius")
    # print(tempval)
    return render_template("orai.html", orask=oraskk, valandinis=tempval)

@app.route("/naujienos")
def naujienos():
    return render_template("naujienos.html")

@app.route("/ciklas")
def ciklas():
    return render_template("ciklas.html")

@app.route("/pasisveikink5", methods=["GET", "POST"]) ###########################
def pasisveikink5():
    if request.method == "GET":
        return render_template("pasisveikink5.html")
    if request.method == "POST":
        var = request.form["vardas5"]
        return render_template("ciklas2.html", var=var)


# @app.route("/ciklas2")
# def user():
#     return render_template("ciklas2.html")


@app.route("/<kintamasis>")
def user(kintamasis):
    return render_template("vardas.html", sablono_kint=kintamasis)

if __name__ == "__main__":
    app.run()