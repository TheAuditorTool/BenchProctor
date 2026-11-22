# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
import jsonschema
from flask import request, jsonify


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00156", methods=["POST"])
def BenchmarkTest00156():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ' '.join(parts)
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session.update({'data': str(processed)})
    return jsonify({"result": "success"})
