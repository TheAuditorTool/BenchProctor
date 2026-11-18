# SPDX-License-Identifier: Apache-2.0
from flask import Flask, session
import os
from flask import jsonify


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00036", methods=["POST"])
def BenchmarkTest00036():
    env_value = os.environ.get('APP_INPUT', '')
    data = str(env_value).replace('\x00', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
