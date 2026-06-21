# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest17834():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
