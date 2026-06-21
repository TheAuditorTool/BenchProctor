# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify


def BenchmarkTest03916(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
