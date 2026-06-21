# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def relay_value(value):
    return value

def BenchmarkTest01168(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
