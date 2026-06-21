# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest18708():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
