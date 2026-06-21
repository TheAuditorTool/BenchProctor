# SPDX-License-Identifier: Apache-2.0
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest32938():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
