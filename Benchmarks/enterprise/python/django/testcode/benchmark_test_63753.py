# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest63753(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        return redirect(str(data))
    return JsonResponse({"saved": True})
