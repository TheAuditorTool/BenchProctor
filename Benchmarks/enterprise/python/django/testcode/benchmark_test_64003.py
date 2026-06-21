# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest64003(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
