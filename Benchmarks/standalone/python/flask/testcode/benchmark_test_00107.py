# SPDX-License-Identifier: Apache-2.0
import io
from lxml import etree
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00107", methods=["POST"])
def BenchmarkTest00107():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    for _event, element in etree.iterparse(io.BytesIO(str(data).encode()), events=('end',), load_dtd=True, resolve_entities=True, no_network=False):
        element.clear()
    return jsonify({"result": "success"})
