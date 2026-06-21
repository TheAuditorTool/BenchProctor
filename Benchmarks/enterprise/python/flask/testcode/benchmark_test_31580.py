# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest31580():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
