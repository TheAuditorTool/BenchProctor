# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import json
from flask import request, jsonify


def BenchmarkTest25099():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
