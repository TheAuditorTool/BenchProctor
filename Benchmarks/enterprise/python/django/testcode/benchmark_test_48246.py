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

def BenchmarkTest48246(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    processed = data[:64]
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
