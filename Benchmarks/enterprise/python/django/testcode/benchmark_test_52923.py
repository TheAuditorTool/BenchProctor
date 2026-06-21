# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest52923(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
