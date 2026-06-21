# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import base64
from flask import request, jsonify


def BenchmarkTest01698():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
