# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def BenchmarkTest11402():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(json_value) + '"]')
    return jsonify({"result": "success"})
