# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest37266():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
