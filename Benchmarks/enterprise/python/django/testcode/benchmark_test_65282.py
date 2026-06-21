# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest65282(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
