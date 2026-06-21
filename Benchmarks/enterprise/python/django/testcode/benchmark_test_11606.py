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

def BenchmarkTest11606(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
