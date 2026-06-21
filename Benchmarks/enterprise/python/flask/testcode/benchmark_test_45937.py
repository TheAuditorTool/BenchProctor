# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import os
from flask import jsonify


def BenchmarkTest45937():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
