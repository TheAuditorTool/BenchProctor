# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest75153():
    header_value = request.headers.get('X-Custom-Header', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(header_value).encode(), _parser)
    return jsonify({"result": "success"})
