# SPDX-License-Identifier: Apache-2.0
from flask import Flask, Response
import bleach
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


@app.route("/BenchmarkTest00201", methods=["POST"])
def BenchmarkTest00201():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    processed = bleach.clean(data)
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(processed) + '</div>')
    return resp
