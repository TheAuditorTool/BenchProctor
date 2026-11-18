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


@app.route("/BenchmarkTest00234", methods=["POST"])
def BenchmarkTest00234():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    session['data'] = str(data)
    return jsonify({"result": "success"})
