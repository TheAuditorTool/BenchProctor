# SPDX-License-Identifier: Apache-2.0
import json
import os
from flask import Flask, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00003", methods=["POST"])
def BenchmarkTest00003():
    env_value = os.environ.get('APP_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    parsed = json.loads(data)
    return jsonify({'parsed': str(parsed)}), 200
