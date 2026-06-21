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

def BenchmarkTest66428(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
