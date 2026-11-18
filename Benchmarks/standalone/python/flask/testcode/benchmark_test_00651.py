# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Flask, request, jsonify
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00651", methods=["POST"])
def BenchmarkTest00651():
    header_value = request.headers.get('X-Custom-Header', '')
    parsed = urlparse(header_value)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = header_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
