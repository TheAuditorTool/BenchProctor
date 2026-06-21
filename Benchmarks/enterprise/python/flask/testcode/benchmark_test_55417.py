# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from lxml import etree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest55417():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
