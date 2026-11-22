# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, make_response
from flask import jsonify
import urllib.parse


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00057/<path_param>", methods=["POST"])
def BenchmarkTest00057(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; HttpOnly; SameSite=Strict; Path=/'
    return resp
