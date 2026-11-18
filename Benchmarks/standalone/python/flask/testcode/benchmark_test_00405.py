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


@app.route("/BenchmarkTest00405", methods=["POST"])
def BenchmarkTest00405():
    auth_header = request.headers.get('Authorization', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
