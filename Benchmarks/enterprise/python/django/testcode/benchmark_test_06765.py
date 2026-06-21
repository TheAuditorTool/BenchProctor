# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest06765(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
