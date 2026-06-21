# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest32072(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
