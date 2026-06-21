# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest22638(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
