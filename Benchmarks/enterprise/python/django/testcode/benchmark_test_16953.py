# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest16953(request):
    upload_name = request.FILES['upload'].name
    data = ensure_str(upload_name)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
