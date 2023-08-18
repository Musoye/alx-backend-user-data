#!/usr/bin/env python3
"""flask app for suthentication"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    """Get the index page"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
