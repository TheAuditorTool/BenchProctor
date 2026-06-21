# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59008(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
