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
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ' '.join(parts)
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(data) + '</div>')
    return resp
