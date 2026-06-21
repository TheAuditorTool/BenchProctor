# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def to_text(value):
    return str(value).strip()

def BenchmarkTest10562(request):
    xml_value = request.body.decode('utf-8')
    data = to_text(xml_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
