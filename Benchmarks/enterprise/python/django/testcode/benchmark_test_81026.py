# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


request_state: dict[str, str] = {}

def BenchmarkTest81026(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
