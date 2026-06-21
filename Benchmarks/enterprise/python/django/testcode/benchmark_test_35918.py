# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest35918(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(env_value)), context=ctx)
    return JsonResponse({"saved": True})
