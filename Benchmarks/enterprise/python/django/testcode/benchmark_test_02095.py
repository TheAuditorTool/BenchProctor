# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest02095(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})
