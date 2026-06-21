# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest81320():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
