# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from dataclasses import dataclass
from flask import Flask, request, jsonify
import re


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00057", methods=["POST"])
def BenchmarkTest00057():
    header_value = request.headers.get('X-Custom-Header', '')
    form = FormData(payload=header_value)
    data = form.payload
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
