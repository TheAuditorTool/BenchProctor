# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest14607(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    request_state['last_input'] = prop_value
    data = request_state['last_input']
    auth_check('user', data)
    return JsonResponse({"saved": True})
