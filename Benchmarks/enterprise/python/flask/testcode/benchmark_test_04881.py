# SPDX-License-Identifier: Apache-2.0
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest04881():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
