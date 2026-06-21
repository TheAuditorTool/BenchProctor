# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest23606(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
