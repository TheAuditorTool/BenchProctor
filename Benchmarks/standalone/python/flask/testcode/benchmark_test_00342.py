# SPDX-License-Identifier: Apache-2.0
from Crypto.Hash import MD4
from flask import Flask, request, jsonify


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


@app.route("/BenchmarkTest00342", methods=["POST"])
def BenchmarkTest00342():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    digest = MD4.new(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
