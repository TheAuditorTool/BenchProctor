# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def coalesce_blank(value):
    return value or ''

def BenchmarkTest50107(request):
    user_id = request.GET.get('id', '')
    data = coalesce_blank(user_id)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
