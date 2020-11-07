from flask import Flask, render_template

app = Flask(__name__)
app.config["FREEZER_DESTINATION"] = "docs"


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/services.html")
def services():
    return render_template("services.html")


@app.route("/bus.html")
def bus():
    return render_template("bus.html")


if __name__ == "__main__":
    app.run(debug=True)