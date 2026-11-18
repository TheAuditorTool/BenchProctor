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


@app.route("/BenchmarkTest00199", methods=["POST"])
def BenchmarkTest00199():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(json_value).strip()
        case _:
            data = str(json_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
