# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest17015(request, path_param):
    path_value = path_param
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(path_value)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
