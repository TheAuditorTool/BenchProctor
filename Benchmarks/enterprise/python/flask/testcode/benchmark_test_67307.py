# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def BenchmarkTest67307():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
