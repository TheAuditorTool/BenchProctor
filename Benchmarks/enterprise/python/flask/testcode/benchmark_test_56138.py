# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import re
from flask import jsonify


def BenchmarkTest56138(path_param):
    path_value = path_param
    data = f'{path_value}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
