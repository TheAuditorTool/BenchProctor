# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, validate, ValidationError


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00192", methods=["POST"])
def BenchmarkTest00192():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.%~\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
