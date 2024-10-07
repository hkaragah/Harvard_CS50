from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/hello", methods=["POST"]) # users submit data via "post" moethod to the "hello" function
# def hello():
#     name = request.form.get("name").capitalize() # get the part of the form called "name"
#     return render_template("hello.html", name=name)


@app.route("/hello", methods=["GET", "POST"]) # users submit data via "get" and "post" moethods to the "hello" function
def hello():
    if request.method == "POST":
        name = request.form.get("name").capitalize()
        return render_template("hello.html", name=name)
    else:
        return "Please submit the form instead."



if __name__ == "__main__":
    app.run(debug=True)