# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json
import os
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest34636(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return asyncio.run(_evasion_task())
