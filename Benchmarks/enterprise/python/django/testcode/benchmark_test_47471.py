# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest47471(request, path_param):
    path_value = path_param
    data = default_blank(path_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
