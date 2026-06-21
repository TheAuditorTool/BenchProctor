# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify


def BenchmarkTest17476(path_param):
    path_value = path_param
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(path_value) + '"]')
    return jsonify({"result": "success"})
