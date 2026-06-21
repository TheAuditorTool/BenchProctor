# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest14151(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
