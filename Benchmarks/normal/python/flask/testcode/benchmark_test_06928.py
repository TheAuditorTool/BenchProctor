# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import ast
from lxml import etree


def BenchmarkTest06928():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
