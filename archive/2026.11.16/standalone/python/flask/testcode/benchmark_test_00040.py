# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import requests
from flask import Flask, jsonify
import socket
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00040", methods=["POST"])
def BenchmarkTest00040():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data, _sep, _rest = str(api_value).partition('\x00')
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
