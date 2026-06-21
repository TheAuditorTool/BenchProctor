# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import os
from flask import jsonify


def BenchmarkTest28035():
    env_value = os.environ.get('USER_INPUT', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(env_value) + '"]')
    return jsonify({"result": "success"})
