# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest05354(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ctx = RequestContext(argv_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
