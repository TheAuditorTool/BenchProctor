# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest63368(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
