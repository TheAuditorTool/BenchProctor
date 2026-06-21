# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest42952(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    requests.get(str(data))
    return JsonResponse({"saved": True})
