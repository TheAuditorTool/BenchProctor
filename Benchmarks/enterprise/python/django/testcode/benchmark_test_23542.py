# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest23542(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
