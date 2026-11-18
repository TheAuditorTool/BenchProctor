# SPDX-License-Identifier: Apache-2.0
import os
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


@app.route("/BenchmarkTest00309", methods=["POST"])
def BenchmarkTest00309():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
