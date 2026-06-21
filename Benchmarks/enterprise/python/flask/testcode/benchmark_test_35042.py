# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import os
from flask import jsonify


def BenchmarkTest35042():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
