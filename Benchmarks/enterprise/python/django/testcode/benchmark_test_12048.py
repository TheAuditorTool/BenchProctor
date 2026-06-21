# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12048(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
