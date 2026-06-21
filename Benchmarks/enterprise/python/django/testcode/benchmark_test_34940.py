# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest34940(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
