# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest48327(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    auth_check('user', data)
    return JsonResponse({"saved": True})
