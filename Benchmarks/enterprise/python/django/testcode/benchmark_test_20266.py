# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def BenchmarkTest20266(request):
    xml_value = request.body.decode('utf-8')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(xml_value))
    return JsonResponse({"saved": True})
