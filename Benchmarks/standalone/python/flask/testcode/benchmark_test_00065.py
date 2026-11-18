# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
from lxml import etree


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00065", methods=["POST"])
def BenchmarkTest00065():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
