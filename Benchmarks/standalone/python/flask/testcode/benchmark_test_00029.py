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


@app.route("/BenchmarkTest00029", methods=["POST"])
def BenchmarkTest00029():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
