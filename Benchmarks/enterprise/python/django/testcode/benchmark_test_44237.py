# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest44237(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
