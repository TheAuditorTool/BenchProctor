# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10364(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
