# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest07425(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
