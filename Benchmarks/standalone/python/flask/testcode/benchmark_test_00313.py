# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, request, jsonify
from pydantic import Field, ValidationError, create_model


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00313", methods=["POST"])
def BenchmarkTest00313():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%\\-]+$")))(value=str(data))
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
