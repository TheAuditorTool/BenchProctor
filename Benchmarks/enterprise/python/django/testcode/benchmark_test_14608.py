# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest14608(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = handle(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
