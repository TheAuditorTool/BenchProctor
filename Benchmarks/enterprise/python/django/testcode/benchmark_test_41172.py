# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest41172(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = handle(cookie_value)
    processed = str(data).replace("<script", "")
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
