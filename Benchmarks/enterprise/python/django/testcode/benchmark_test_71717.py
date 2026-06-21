# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest71717(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
