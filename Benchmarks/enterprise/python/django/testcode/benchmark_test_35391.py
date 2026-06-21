# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest35391(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
