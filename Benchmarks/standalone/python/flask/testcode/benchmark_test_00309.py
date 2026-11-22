# SPDX-License-Identifier: Apache-2.0
from flask import Flask, current_app
import re
from flask import request, jsonify


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
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    current_app.config['ACTIVE_TENANT'] = str(processed)
    return jsonify({"result": "success"})
