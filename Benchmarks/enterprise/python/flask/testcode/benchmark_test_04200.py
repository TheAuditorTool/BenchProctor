# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest04200():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
