# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def BenchmarkTest54090():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
