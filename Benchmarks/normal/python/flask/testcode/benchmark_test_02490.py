# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def normalise_input(value):
    return value.strip()

def BenchmarkTest02490():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
