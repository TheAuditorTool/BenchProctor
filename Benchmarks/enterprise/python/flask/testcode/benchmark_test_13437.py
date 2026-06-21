# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest13437():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
