# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest13514(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = handle(cookie_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
