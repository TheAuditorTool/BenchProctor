# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest79651(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
