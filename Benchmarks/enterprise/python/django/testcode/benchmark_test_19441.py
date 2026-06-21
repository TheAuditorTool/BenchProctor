# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest19441(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    os.remove(str(data))
    return JsonResponse({"saved": True})
