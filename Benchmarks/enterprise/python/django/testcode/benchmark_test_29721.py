# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest29721(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
