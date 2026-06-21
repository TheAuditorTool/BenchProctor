# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest71393(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
