# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import re
from pathlib import Path


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00208", methods=["POST"])
def BenchmarkTest00208():
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch("^(asc|desc|name|created)$", str(cookie_value)):
        return jsonify({'error': 'forbidden'}), 400
    processed = cookie_value
    Path('/var/app/data/' + str(processed)).write_text('data')
    return jsonify({"result": "success"})
