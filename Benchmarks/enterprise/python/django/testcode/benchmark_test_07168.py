# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest07168(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
