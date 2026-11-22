# SPDX-License-Identifier: Apache-2.0
import io
import defusedxml.ElementTree
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00122", methods=["POST"])
def BenchmarkTest00122():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    for _event, element in defusedxml.ElementTree.iterparse(io.BytesIO(str(data).encode()), events=('end',)):
        element.clear()
    return jsonify({"result": "success"})
