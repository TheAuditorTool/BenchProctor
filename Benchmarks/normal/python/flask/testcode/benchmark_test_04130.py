# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def BenchmarkTest04130():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
