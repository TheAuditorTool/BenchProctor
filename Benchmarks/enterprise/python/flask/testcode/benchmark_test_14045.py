# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest14045():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
