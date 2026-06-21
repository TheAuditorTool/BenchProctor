# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import json


def BenchmarkTest51008(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
