# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest00764(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
