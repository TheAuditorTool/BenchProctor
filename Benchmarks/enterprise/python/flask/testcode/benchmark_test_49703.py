# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest49703():
    host_value = request.headers.get('Host', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(host_value).encode(), _parser)
    return jsonify({"result": "success"})
