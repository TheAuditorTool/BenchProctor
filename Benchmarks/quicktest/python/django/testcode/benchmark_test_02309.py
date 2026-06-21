# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02309(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
