# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest17430(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
