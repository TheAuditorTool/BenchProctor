# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest74839(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
