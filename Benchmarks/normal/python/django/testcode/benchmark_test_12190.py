# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import urllib.request


def BenchmarkTest12190(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
