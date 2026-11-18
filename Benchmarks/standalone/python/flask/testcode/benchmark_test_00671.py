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


@app.route("/BenchmarkTest00671", methods=["POST"])
def BenchmarkTest00671():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
