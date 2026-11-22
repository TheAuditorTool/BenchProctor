# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
from pathlib import Path


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00040", methods=["POST"])
def BenchmarkTest00040():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    Path(checked_path).write_text('data')
    return jsonify({"result": "success"})
