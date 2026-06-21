# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
from app_runtime import auth_check


def BenchmarkTest75104(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
