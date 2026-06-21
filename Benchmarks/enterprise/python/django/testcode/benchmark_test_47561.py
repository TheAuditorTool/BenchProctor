# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest47561(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
