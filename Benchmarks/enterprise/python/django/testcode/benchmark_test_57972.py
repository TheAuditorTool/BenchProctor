# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest57972(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    auth_check('user', data)
    return JsonResponse({"saved": True})
