# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00351", methods=["POST"])
def BenchmarkTest00351():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header!s}'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
