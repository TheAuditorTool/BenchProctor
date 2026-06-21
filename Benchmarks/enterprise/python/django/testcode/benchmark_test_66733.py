# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def coalesce_blank(value):
    return value or ''

def BenchmarkTest66733(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
