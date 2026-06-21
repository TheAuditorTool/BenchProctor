# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest78171(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = bytearray(int(env_value) if str(env_value).isdigit() else 0)
    return JsonResponse({"saved": True})
