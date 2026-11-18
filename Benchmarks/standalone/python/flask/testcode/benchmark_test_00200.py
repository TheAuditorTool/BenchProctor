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


@app.route("/BenchmarkTest00200", methods=["POST"])
def BenchmarkTest00200():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
