# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from lxml import etree


def ensure_str(value):
    return str(value)

def BenchmarkTest57339():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
