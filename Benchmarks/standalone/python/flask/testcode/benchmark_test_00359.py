# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Flask, request, jsonify
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00359", methods=["POST"])
def BenchmarkTest00359():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
