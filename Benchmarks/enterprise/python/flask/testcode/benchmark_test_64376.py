# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def to_text(value):
    return str(value).strip()

def BenchmarkTest64376():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
