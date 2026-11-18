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


@app.route("/BenchmarkTest00660", methods=["POST"])
def BenchmarkTest00660():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.%~\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
