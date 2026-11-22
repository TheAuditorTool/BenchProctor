# SPDX-License-Identifier: Apache-2.0
import os
from http.cookies import SimpleCookie
from flask import Flask, make_response
from flask import jsonify


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


@app.route("/BenchmarkTest00047/<path_param>", methods=["POST"])
def BenchmarkTest00047(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    cookie = SimpleCookie()
    cookie['session'] = str(data)
    cookie['session'].update({'httponly': True, 'samesite': 'Strict', 'path': '/'})
    resp = make_response(jsonify({'status': 'ok'}))
    resp.headers.add('Set-Cookie', cookie['session'].OutputString())
    return resp
