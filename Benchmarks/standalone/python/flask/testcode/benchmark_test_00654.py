# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
from flask import request, jsonify
import re


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00654", methods=["POST"])
def BenchmarkTest00654():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
