# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00010", methods=["POST"])
def BenchmarkTest00010():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
