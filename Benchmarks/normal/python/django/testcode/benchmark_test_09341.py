# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09341(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    os.seteuid(65534)
    return JsonResponse({"saved": True})
