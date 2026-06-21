# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest43542():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    def _primary():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
