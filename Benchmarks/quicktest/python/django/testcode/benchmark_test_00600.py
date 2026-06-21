# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00600(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
