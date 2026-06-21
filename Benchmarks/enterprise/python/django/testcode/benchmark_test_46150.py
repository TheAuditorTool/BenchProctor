# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import json
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest46150(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    if time.time() > 1000000000:
        return redirect(str(data))
    return JsonResponse({"saved": True})
