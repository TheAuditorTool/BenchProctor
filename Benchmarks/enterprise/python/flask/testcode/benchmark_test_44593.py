# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest44593():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
