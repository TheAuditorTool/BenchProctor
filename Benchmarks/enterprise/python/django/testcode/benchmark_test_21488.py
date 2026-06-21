# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest21488(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
