# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest65855():
    referer_value = request.headers.get('Referer', '')
    data = default_blank(referer_value)
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
