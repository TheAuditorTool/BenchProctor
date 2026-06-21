# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02344(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
