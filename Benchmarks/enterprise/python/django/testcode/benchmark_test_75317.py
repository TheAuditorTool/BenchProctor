# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest75317(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ctx = RequestContext(argv_value)
    data = ctx.payload
    processed = data[:64]
    os.unlink('/var/app/data/' + str(processed))
    return JsonResponse({"saved": True})
