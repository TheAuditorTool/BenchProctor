# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest16991(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
