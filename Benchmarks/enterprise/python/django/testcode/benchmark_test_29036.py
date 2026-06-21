# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest29036(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    eval(compile("subprocess.run([str(data), '--status'], shell=False)", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
