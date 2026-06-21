# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest03129():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\[\\]\'\\"=_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
