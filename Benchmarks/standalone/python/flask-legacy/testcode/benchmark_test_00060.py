# SPDX-License-Identifier: Apache-2.0
import io
import defusedxml.ElementTree
from dataclasses import dataclass
from flask import Flask, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00060", methods=["POST"])
def BenchmarkTest00060():
    xml_value = request.get_data(as_text=True)
    form = FormData(payload=xml_value)
    data = form.payload
    for _event, element in defusedxml.ElementTree.iterparse(io.BytesIO(str(data).encode()), events=('end',)):
        element.clear()
    return jsonify({"result": "success"})
