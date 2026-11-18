# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
from urllib.parse import urlparse
import requests
from flask import jsonify
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00042", methods=["POST"])
def BenchmarkTest00042():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    if api_value:
        data = api_value
    else:
        data = ''
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
