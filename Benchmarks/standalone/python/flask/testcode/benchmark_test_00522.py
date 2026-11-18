# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00522", methods=["POST"])
def BenchmarkTest00522():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        jsonschema.validate(str(header_value), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = header_value
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
