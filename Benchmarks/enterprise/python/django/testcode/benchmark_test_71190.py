# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest71190(request):
    env_value = os.environ.get('USER_INPUT', '')
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(env_value)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
