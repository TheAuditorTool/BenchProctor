# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def ensure_str(value):
    return str(value)

def BenchmarkTest71535():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
