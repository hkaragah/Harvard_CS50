from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


# The following block of code can be removed and instead run "flask -app application.py run" in the terminal command line
if __name__ == "__main__":
    app.run(debug=True)
    