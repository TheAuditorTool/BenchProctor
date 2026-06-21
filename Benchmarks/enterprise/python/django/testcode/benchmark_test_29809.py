# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest29809(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
