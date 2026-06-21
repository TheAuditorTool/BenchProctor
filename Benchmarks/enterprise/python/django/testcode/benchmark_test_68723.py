# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest68723(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    processed = data[:64]
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return JsonResponse({"saved": True})
