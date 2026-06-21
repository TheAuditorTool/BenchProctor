# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest69656(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = handle(host_value)
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return JsonResponse({"saved": True})
