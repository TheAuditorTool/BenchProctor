# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify


def BenchmarkTest38338(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
