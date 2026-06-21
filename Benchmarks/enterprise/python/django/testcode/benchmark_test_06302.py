# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest06302(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
