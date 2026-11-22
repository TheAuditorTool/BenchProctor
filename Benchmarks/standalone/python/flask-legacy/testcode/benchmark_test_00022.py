# SPDX-License-Identifier: Apache-2.0
import os
from http.cookies import SimpleCookie
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


@app.route("/BenchmarkTest00022", methods=["POST"])
def BenchmarkTest00022():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    cookie = SimpleCookie()
    cookie['session'] = str(data)
    cookie['session'].update({'secure': True, 'httponly': True, 'samesite': 'Strict', 'path': '/'})
    resp = make_response(jsonify({'status': 'ok'}))
    resp.headers.add('Set-Cookie', cookie['session'].OutputString())
    return resp
