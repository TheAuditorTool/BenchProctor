# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest16931():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    if time.time() > 1000000000:
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
