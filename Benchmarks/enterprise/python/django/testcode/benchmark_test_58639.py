# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest58639(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
