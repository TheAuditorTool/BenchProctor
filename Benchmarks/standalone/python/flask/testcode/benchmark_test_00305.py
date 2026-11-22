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


@app.route("/BenchmarkTest00305", methods=["POST"])
def BenchmarkTest00305():
    raw_body = request.get_data(as_text=True)
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    for _event, element in etree.iterparse(io.BytesIO(str(data).encode()), events=('end',), load_dtd=True, resolve_entities=True, no_network=False):
        element.clear()
    return jsonify({"result": "success"})
