# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest43276(request):
    host_value = request.META.get('HTTP_HOST', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
