# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest43468():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
