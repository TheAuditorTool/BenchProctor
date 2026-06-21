# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest01162(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ' '.join(str(json_value).split())
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
