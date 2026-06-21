# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


request_state: dict[str, str] = {}

def BenchmarkTest17298(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
