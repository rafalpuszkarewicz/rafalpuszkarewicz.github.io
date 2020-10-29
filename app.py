from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/services.html")
def services():
    return render_template("services.html"), {
        "Content-Type": "text/html; charset=utf-8"
    }


if __name__ == "__main__":
    app.run(debug=True)