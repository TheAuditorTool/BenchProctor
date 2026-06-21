# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import os
from flask import jsonify


def BenchmarkTest66974():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
