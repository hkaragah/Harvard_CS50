
# Simple web application

from flask import Flask

app = Flask(__name__) # create new web app of type Flask web app, __name__ represents the current file: current file is the web app

@app.route("/") # default page, when user goes to default page run the following function @ is a decorator
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)