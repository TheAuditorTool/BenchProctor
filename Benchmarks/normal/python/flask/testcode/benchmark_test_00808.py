# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest00808():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = relay_value(json_value)
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
