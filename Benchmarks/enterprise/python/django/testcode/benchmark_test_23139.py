# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest23139(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
