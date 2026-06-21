# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import re
from flask import request, jsonify


def BenchmarkTest60953():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
