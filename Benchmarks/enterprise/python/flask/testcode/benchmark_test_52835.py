# SPDX-License-Identifier: Apache-2.0
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest52835():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
