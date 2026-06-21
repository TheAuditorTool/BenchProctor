# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest22286():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
