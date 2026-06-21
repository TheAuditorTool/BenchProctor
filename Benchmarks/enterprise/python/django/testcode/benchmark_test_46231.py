# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest46231(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
