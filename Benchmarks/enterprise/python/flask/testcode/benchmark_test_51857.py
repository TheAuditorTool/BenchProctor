# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest51857():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = default_blank(json_value)
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
