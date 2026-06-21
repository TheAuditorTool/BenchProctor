# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest04742():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
