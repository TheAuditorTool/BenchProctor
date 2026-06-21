# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest17103():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
