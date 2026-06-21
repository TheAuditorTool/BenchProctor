# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13826(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
