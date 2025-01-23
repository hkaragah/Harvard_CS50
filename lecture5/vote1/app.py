import os
import socket
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("HARVARD_CS50_LECTURE5_DB_URL")

# Initialize SocketIO that will allow for real-time communication between clients and server
# It broadcast events to others and listens for events from others
socketio = SocketIO(app)

votes = {"yes": 0, "no": 0, "maybe": 0}

@app.route("/")
def index():
    return render_template("index.html", votes=votes)

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    votes[selection] += 1
    # Emit an event to all clients that a vote has been submitted
    # All people who are connected to the server will receive this event
    # and get the updated vote count
    emit("vote totals", votes, broadcast=True)