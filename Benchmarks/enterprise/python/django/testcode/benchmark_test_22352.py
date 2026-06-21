# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest22352(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
