# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def BenchmarkTest12825():
    cookie_value = request.cookies.get('session_token', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(cookie_value) + '"]')
    return jsonify({"result": "success"})
