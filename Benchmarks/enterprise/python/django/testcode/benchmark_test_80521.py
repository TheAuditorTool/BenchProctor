# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest80521(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
