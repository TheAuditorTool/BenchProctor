# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def BenchmarkTest07479(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
