# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import re
from flask import request, jsonify


def BenchmarkTest07920():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
