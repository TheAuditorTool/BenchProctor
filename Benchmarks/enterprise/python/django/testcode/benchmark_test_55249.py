# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest55249(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
