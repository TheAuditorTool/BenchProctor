# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request


def BenchmarkTest41433(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json.loads(json_value).get('value', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
