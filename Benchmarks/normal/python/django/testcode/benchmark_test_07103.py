# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest07103(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
