# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify


def BenchmarkTest79110(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
