# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest58217():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
