# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, make_response
from flask import request, jsonify
import json


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00178", methods=["POST"])
def BenchmarkTest00178():
    user_id = request.args.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
