# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import requests
from flask import Flask, jsonify
import socket
import urllib.parse
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00105", methods=["POST"])
def BenchmarkTest00105():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    pending = list(str(api_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((urllib.parse.urlparse(str(target_url)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
