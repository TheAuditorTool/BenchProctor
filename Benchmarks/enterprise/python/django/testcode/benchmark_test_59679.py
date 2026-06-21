# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest59679(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    requests.get(str(data))
    return JsonResponse({"saved": True})
