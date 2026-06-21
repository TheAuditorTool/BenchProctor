# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest60043(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
