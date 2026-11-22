# SPDX-License-Identifier: Apache-2.0
import re
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


@app.route("/BenchmarkTest00287", methods=["POST"])
def BenchmarkTest00287():
    ua_value = request.headers.get('User-Agent', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", ua_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = ua_value
    Path('/var/app/data/' + str(processed)).write_text('data')
    return jsonify({"result": "success"})
