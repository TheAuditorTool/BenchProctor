# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest48298(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    exec(str(data))
    return JsonResponse({"saved": True})
