# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import re
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00080", methods=["POST"])
def BenchmarkTest00080():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute('SELECT * FROM users ORDER BY ' + str(processed))
    return jsonify({"result": "success"})
