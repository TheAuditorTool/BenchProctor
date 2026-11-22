# SPDX-License-Identifier: Apache-2.0
import re
from flask import Flask, request, jsonify
from flask import render_template_string


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00094", methods=["POST"])
def BenchmarkTest00094():
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string('<div>{{ value|safe }}</div>', value=str(processed))
