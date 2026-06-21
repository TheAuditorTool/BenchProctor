# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import urllib.request


@dataclass
class FormData:
    payload: str

def BenchmarkTest47536(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
