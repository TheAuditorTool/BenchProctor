# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def relay_value(value):
    return value

def BenchmarkTest07390(request):
    user_id = request.GET.get('id', '')
    data = relay_value(user_id)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
