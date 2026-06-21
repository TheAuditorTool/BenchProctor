# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
from app_runtime import auth_check


def BenchmarkTest34654(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
