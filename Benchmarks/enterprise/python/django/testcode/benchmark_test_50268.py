# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest50268(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
