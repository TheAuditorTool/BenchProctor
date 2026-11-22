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


@app.route("/BenchmarkTest00243", methods=["POST"])
def BenchmarkTest00243():
    user_id = request.args.get('id', '')
    match = re.match(r'^[^@]+@([^@]+)$', str(user_id))
    if match is None:
        return jsonify({'error': 'not an email address'}), 400
    domain = match.group(1)
    return jsonify({'domain': domain}), 200
