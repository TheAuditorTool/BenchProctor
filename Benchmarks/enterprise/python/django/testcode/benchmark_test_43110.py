# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest43110(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
