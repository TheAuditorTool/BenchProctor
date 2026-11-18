# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, make_response
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00236", methods=["POST"])
def BenchmarkTest00236():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    form = FormData(payload=graphql_var)
    data = form.payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
