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


@app.route("/BenchmarkTest00255", methods=["POST"])
def BenchmarkTest00255():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
