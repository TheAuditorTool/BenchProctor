# SPDX-License-Identifier: Apache-2.0
import re
from flask import Flask, request, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00024", methods=["POST"])
def BenchmarkTest00024():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute("SELECT * FROM users WHERE id = '" + str(processed) + "'")
    return jsonify({"result": "success"})
