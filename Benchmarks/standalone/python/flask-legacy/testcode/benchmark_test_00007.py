# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Flask, request
from flask import render_template_string
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00007", methods=["POST"])
def BenchmarkTest00007():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    return render_template_string('<div>{{ value|safe }}</div>', value=str(data))
