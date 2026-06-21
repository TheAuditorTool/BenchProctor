# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest75802(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
