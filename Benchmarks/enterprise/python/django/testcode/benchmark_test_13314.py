# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def BenchmarkTest13314(request, path_param):
    path_value = path_param
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(path_value))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
