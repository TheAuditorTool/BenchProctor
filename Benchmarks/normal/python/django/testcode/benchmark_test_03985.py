# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest03985(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
