from flask import Flask, render_template, url_for
from req import get_names, URL_NAMES


app = Flask(__name__)

@app.route("/")
def index():
    names = get_names(URL_NAMES)
    return render_template('index.html', names=names)

@app.route("/<int:year>")
def index_filter(year):
    print(type(year))
    names = get_names(URL_NAMES, year)
    return render_template('index.html', names=names, year=year)

if __name__ == "__main__":
    app.run(debug=True)