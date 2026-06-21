# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest17411():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
