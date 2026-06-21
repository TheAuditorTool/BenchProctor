# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest26042():
    origin_value = request.headers.get('Origin', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(origin_value).encode(), _parser)
    return jsonify({"result": "success"})
