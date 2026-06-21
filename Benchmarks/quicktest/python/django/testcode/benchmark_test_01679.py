# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest01679(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
