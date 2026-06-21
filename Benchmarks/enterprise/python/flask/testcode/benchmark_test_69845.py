# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest69845():
    xml_value = request.get_data(as_text=True)
    ctx = RequestContext(xml_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
