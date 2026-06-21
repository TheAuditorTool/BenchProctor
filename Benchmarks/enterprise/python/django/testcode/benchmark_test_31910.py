# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest31910(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    int(str(data))
    return JsonResponse({"saved": True})
