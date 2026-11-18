# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00027", methods=["POST"])
def BenchmarkTest00027():
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(cookie_value).strip()
        case _:
            data = str(cookie_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
