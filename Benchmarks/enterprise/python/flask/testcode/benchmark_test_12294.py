# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12294():
    origin_value = request.headers.get('Origin', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    _ev = {}
    eval(compile("link_path = os.path.join('/var/app/data', str(data))\ntarget = os.readlink(link_path)\nwith open(target, 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
