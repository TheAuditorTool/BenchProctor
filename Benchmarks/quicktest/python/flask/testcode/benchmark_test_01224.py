# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest01224():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
