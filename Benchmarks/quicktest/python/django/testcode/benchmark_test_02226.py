# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02226(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
