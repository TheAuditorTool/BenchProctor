# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest21489(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
