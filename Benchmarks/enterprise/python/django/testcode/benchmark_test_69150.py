# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import urllib.request


def BenchmarkTest69150(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
