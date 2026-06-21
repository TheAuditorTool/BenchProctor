# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest05535(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
