# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
import re
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00224", methods=["POST"])
def BenchmarkTest00224():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session.update({'data': str(processed)})
    return jsonify({"result": "success"})
