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


@app.route("/BenchmarkTest00220", methods=["POST"])
def BenchmarkTest00220():
    xml_value = request.get_data(as_text=True)
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(xml_value).strip()
        case _:
            data = str(xml_value)
    parser = defusedxml.sax.make_parser()
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return jsonify({"result": "success"})
