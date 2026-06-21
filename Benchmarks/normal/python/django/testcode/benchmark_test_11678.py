# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest11678(request):
    host_value = request.META.get('HTTP_HOST', '')
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(host_value)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
