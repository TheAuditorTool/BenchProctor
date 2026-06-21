# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import re
from flask import request, jsonify


def BenchmarkTest62525():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
