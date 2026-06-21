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

def BenchmarkTest81261(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
