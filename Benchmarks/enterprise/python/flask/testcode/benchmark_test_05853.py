# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest05853():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
