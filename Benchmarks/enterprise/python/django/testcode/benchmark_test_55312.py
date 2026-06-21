# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest55312(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
