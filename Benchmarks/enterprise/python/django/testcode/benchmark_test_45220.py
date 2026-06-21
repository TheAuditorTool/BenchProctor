# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest45220(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    os.remove(str(data))
    return JsonResponse({"saved": True})
