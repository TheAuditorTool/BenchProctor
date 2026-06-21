# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify


def BenchmarkTest08857(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
