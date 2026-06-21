# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request


def BenchmarkTest50408(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(json_value)).read()
    return JsonResponse({"saved": True})
