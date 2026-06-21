# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


request_state: dict[str, str] = {}

def BenchmarkTest63652(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
