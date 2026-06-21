# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest40025(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
