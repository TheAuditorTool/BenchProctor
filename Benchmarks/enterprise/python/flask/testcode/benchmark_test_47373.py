# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest47373():
    auth_header = request.headers.get('Authorization', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(auth_header).encode(), _parser)
    return jsonify({"result": "success"})
