from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# notes = []
# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         notes.append(request.form.get("note"))
#     return render_template("index.html", notes = notes)


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        session["notes"].append(request.form.get("note"))
    return render_template("index.html", notes = session["notes"])

if __name__ == "__main__":
    app.run(debug=True)