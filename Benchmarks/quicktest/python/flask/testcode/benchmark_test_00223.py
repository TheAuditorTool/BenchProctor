# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import os
from flask import jsonify


def BenchmarkTest00223():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
