# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import requests


def BenchmarkTest81289(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
