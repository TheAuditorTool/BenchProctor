# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest47043(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    if time.time() > 1000000000:
        return redirect(str(data))
    return JsonResponse({"saved": True})
