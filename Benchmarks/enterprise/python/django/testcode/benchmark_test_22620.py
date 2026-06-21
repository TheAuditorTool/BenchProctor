# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest22620(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
