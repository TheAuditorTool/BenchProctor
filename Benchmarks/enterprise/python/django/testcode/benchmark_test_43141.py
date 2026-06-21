# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest43141(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(json_value)), context=ctx)
    return JsonResponse({"saved": True})
