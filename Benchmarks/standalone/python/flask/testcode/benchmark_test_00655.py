# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
from flask import jsonify
from pydantic import Field, ValidationError, create_model
from app_runtime import db


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00655", methods=["POST"])
def BenchmarkTest00655():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.\\-]+$")))(value=str(data))
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
