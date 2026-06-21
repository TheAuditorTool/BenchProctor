# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest69188(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
