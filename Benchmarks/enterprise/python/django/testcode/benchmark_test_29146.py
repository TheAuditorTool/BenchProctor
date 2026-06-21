# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest29146(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    auth_check('user', data)
    return JsonResponse({"saved": True})
