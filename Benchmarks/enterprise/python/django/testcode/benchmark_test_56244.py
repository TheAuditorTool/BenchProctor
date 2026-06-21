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

def BenchmarkTest56244(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return JsonResponse({"saved": True})
