# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest65251():
    ua_value = request.headers.get('User-Agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
