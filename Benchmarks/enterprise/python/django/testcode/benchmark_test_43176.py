# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest43176(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
