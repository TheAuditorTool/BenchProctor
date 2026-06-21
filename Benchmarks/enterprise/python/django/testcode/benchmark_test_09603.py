# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest09603(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        result = int(str(env_value))
    except Exception:
        pass
    return JsonResponse({"saved": True})
