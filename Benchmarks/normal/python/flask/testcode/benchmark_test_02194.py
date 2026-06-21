# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from lxml import etree


def relay_value(value):
    return value

def BenchmarkTest02194():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
