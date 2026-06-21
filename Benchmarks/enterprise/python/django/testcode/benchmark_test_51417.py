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

def BenchmarkTest51417(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    os.remove(str(data))
    return JsonResponse({"saved": True})
