# SPDX-License-Identifier: Apache-2.0
import io
import xml.sax
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00083", methods=["POST"])
def BenchmarkTest00083():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_external_ges, True)
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return jsonify({"result": "success"})
