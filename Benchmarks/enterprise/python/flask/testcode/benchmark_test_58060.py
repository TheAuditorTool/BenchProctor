# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def BenchmarkTest58060():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
