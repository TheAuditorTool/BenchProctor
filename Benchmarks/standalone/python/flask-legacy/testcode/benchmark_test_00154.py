# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00154", methods=["POST"])
def BenchmarkTest00154():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    kind = 'json' if str(api_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(api_value).strip()
        case _:
            data = str(api_value)
    return '', 302, {'Location': str(data)}
