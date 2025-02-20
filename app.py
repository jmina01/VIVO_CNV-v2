from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pagos")
def pagos():
    return render_template("pagos.html")

@app.route("/preline.js")
def serve_preline_js():
    return send_from_directory("node_modules/preline/dist", "preline.js")

@app.route("/temp")
def temp():
    return render_template("temp.html")

if __name__ == "__main__":
    app.run(debug=True)
