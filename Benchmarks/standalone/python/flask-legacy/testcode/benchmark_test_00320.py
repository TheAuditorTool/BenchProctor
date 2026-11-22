# SPDX-License-Identifier: Apache-2.0
from flask import Flask, Response
import bleach
import json
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


@app.route("/BenchmarkTest00320", methods=["POST"])
def BenchmarkTest00320():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    processed = bleach.clean(data)
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(processed) + '</div>')
    return resp
