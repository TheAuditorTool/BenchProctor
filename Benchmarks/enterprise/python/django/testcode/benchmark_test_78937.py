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

def BenchmarkTest78937(request):
    xml_value = request.body.decode('utf-8')
    data = handle(xml_value)
    checked_path = os.path.normpath(data)
    with open('/var/uploads/' + str(checked_path), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
