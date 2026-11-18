# SPDX-License-Identifier: Apache-2.0
import re
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00277", methods=["POST"])
def BenchmarkTest00277():
    ua_value = request.headers.get('User-Agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<div>' + str(processed) + '</div>'
