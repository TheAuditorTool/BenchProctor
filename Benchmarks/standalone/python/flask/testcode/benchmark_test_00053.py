# SPDX-License-Identifier: Apache-2.0
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


@app.route("/BenchmarkTest00053", methods=["POST"])
def BenchmarkTest00053():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<div>' + str(processed) + '</div>'
