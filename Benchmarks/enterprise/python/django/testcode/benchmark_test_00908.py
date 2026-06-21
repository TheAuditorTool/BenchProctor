# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00908(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    eval(compile('with open(\'plugins/generated_config.py\', \'w\') as fh:\n    fh.write(\'SETTING = "\' + str(data) + \'"\')\nrunpy.run_path(\'plugins/generated_config.py\')', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
