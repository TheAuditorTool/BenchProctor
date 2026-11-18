# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
from flask import request, jsonify


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00366", methods=["POST"])
def BenchmarkTest00366():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
