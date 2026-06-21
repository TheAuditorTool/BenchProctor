# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
import urllib.request


@dataclass
class FormData:
    payload: str

def BenchmarkTest59909(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
