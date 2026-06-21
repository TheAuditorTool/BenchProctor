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

def BenchmarkTest61168(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
