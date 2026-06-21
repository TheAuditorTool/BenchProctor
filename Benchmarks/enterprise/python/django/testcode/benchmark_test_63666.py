# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest63666(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
