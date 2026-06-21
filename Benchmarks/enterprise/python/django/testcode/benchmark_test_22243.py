# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest22243(request):
    env_value = os.environ.get('USER_INPUT', '')
    os.remove(str(env_value))
    return JsonResponse({"saved": True})
