# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest36395(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    request_state['last_input'] = file_value
    data = request_state['last_input']
    auth_check('user', data)
    return JsonResponse({"saved": True})
