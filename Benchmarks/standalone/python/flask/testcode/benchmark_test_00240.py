# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
import re
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


@app.route("/BenchmarkTest00240", methods=["POST"])
def BenchmarkTest00240():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
