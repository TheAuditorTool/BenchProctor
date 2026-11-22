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


@app.route("/BenchmarkTest00263", methods=["POST"])
def BenchmarkTest00263():
    raw_body = request.get_data(as_text=True)
    if not re.fullmatch("^(asc|desc|name|created)$", str(raw_body)):
        return jsonify({'error': 'forbidden'}), 400
    processed = raw_body
    eval(str(processed))
    return jsonify({"result": "success"})
