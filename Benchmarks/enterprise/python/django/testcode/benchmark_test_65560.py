# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import urllib.request


def BenchmarkTest65560(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
