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

def BenchmarkTest25884(request):
    xml_value = request.body.decode('utf-8')
    data = handle(xml_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
