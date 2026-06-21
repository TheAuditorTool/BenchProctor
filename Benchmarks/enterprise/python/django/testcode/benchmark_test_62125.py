# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest62125(request):
    env_value = os.environ.get('USER_INPUT', '')
    requests.post('http://api.prod.internal/data', data=str(env_value))
    return JsonResponse({"saved": True})
