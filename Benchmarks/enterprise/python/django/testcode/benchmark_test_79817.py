# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79817(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    _ev = {}
    eval(compile("with open(os.path.join('/var/app/data', str(data)), 'r') as fh:\n    content = fh.read()\n_ev['r'] = HttpResponse(content)", '<sink>', 'exec'))
    return _ev['r']
