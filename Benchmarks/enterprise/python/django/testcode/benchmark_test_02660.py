# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02660(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    processed = data[:64]
    globals()['counter'] = int(processed)
    return JsonResponse({"saved": True})
