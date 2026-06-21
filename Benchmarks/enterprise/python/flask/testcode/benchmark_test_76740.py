# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from lxml import etree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest76740(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return jsonify({"result": "success"})
