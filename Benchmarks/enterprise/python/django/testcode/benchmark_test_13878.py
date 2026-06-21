# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13878(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
