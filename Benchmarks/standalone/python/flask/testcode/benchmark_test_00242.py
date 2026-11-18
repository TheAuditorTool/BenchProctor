# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
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


@app.route("/BenchmarkTest00242", methods=["POST"])
def BenchmarkTest00242():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    session['data'] = str(processed)
    return jsonify({"result": "success"})
