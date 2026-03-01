from flask import Flask, render_template, request
from analyzer import analyze_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        message = request.form["message"]
        result = analyze_text(message)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)