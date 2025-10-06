from Flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    arr = ["Herrera", "Gregorio", "slone"]
    autor = "victor 0"
    return render_template("index.html", nombre = autor, amigos = arr)


if __name__ == "__main__":
    app.run(debug=true)
    