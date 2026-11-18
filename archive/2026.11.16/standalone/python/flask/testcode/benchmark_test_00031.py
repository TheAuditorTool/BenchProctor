# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00031", methods=["POST"])
def BenchmarkTest00031():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    processed = bleach.clean(markdown.markdown(data))
    return '<div>' + str(processed) + '</div>'
