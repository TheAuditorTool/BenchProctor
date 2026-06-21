# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00722(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
