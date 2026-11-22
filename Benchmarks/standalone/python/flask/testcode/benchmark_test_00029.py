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


@app.route("/BenchmarkTest00029", methods=["POST"])
def BenchmarkTest00029():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    if match is None:
        return jsonify({'error': 'not an email address'}), 400
    domain = match.group(1)
    return jsonify({'domain': domain}), 200
