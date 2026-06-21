# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import shlex


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02344(request):
    stdin_value = input('input: ')
    ctx = RequestContext(stdin_value)
    data = ctx.payload
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
