# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest27085(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = handle(cookie_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
