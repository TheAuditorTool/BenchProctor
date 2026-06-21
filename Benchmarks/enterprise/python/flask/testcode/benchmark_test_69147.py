# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def BenchmarkTest69147():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
