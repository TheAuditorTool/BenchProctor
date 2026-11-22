# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, make_response
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


@app.route("/BenchmarkTest00020", methods=["POST"])
def BenchmarkTest00020():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
