# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import urllib.request


def BenchmarkTest74315(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
