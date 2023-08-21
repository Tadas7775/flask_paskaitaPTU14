from flask import Flask, render_template, request

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
    return render_template("orai.html")

@app.route("/ciklas")
def ciklas():
    return render_template("ciklas.html")

@app.route("/ciklas2", methods=["GET", "POST"]) ######################################
def ciklas2():
    return render_template("ciklas2.html")
    if request.method == "GET":
        return render_template("ciklas2.html")
    if request.method == "POST":
        vardas = request.form["laukelis2"]
        return render_template("ciklas2.html", sablono_kint=vardas)

@app.route("/<kintamasis>")
def user(kintamasis):
    return render_template("vardas.html", sablono_kint=kintamasis)

if __name__ == "__main__":
    app.run()