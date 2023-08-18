from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello world, cia mano namu puslapis Pirmas su Flask</h1>"

@app.route("/<kintamasis>")
def user(kintamasis):
    return f"Hello, {kintamasis} welcome to Flask website"

if __name__ == "__main__":
    app.run()