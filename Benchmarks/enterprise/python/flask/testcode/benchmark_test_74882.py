# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import base64
from flask import request, jsonify


def BenchmarkTest74882():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
