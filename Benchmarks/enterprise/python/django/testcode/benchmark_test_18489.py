# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest18489(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
