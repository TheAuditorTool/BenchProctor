# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest32234(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
