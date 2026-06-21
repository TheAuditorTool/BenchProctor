# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest22780(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
