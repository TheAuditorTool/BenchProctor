# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import requests


def BenchmarkTest58339(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
