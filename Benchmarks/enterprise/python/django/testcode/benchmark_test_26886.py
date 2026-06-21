# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest26886(request):
    stdin_value = input('input: ')
    ctx = RequestContext(stdin_value)
    data = ctx.payload
    eval(compile("subprocess.Popen('echo ' + str(data), shell=True).wait()", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
