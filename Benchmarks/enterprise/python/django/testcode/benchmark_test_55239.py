# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest55239(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    exec(str(data))
    return JsonResponse({"saved": True})
