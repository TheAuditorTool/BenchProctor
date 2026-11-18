# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import Flask, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00642", methods=["POST"])
def BenchmarkTest00642():
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % str(env_value)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute("SELECT * FROM users WHERE id = '" + str(processed) + "'")
    return jsonify({"result": "success"})
