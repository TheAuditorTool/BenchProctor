# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def BenchmarkTest30655(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
