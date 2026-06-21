# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import re
from flask import jsonify


def BenchmarkTest17132(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
