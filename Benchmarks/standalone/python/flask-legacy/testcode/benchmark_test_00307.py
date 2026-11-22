# SPDX-License-Identifier: Apache-2.0
from flask import Flask, Response
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00307", methods=["POST"])
def BenchmarkTest00307():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(data) + '</div>')
    return resp
