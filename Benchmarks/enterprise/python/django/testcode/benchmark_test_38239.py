# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import socket


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest38239(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return JsonResponse({"saved": True})
