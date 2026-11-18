# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
from urllib.parse import urlparse
from urllib.parse import unquote
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


@app.route("/BenchmarkTest00129", methods=["POST"])
def BenchmarkTest00129():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
