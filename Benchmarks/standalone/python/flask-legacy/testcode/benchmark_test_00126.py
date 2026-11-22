# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
from urllib.parse import urlparse
from flask import request, jsonify
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00126", methods=["POST"])
def BenchmarkTest00126():
    host_value = request.headers.get('Host', '')
    parsed = urlparse(host_value)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", host_value) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = host_value
    return redirect(str(target_url))
