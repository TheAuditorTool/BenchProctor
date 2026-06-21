# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00726(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
