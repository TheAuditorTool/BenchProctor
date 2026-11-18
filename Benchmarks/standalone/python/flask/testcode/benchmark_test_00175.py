# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import defusedxml.ElementTree


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00175", methods=["POST"])
def BenchmarkTest00175():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
