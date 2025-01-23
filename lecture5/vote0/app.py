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

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    
    # Emit an event to all clients that a vote has been submitted
    # All people who are connected to the server will receive this event
    # and get the updated vote count
    emit("announce vote", {"selection": selection}, broadcast=True)