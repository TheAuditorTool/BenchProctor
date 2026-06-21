# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def relay_value(value):
    return value

def BenchmarkTest31090():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
