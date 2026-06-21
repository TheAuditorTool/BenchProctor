# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest16884(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    int(str(data))
    return JsonResponse({"saved": True})
