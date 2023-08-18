from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/orai")
def orai():
    return render_template("orai.html")



@app.route("/<kintamasis>")
def user(kintamasis):
    return f"Hello, {kintamasis} welcome to Flask website"

if __name__ == "__main__":
    app.run()