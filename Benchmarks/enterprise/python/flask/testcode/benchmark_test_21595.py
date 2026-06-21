# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest21595():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    def _primary():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
