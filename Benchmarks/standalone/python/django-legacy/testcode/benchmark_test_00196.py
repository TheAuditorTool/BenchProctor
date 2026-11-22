# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
import base64


def BenchmarkTest00196(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    outbound = urllib.request.Request(str(data), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
