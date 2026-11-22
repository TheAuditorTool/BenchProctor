# SPDX-License-Identifier: Apache-2.0
import io
import xml.sax
import defusedxml.sax
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
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    parser = defusedxml.sax.make_parser()
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return jsonify({"result": "success"})
