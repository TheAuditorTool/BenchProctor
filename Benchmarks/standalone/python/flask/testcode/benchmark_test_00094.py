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


@app.route("/BenchmarkTest00094", methods=["POST"])
def BenchmarkTest00094():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '{}'.format(json_value)
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(data) + '</div>')
    return resp
