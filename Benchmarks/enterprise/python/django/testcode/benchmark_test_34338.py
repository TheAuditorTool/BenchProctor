# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest34338(request):
    raw_body = request.body.decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
