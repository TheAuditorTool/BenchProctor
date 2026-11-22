# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00229", methods=["POST"])
def BenchmarkTest00229():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    eval(str(data))
    return jsonify({"result": "success"})
