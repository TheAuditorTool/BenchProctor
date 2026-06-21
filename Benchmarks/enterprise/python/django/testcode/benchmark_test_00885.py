# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
import urllib.parse
import ssl


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest00885(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
