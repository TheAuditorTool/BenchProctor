# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest14732():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
