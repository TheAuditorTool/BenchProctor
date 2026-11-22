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


@app.route("/BenchmarkTest00012", methods=["POST"])
def BenchmarkTest00012():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    processed = bleach.clean(data)
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(processed) + '</div>')
    return resp
