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


@app.route("/BenchmarkTest00060", methods=["POST"])
def BenchmarkTest00060():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_external_ges, True)
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return jsonify({"result": "success"})
