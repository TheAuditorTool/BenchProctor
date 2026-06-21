# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def BenchmarkTest49426(request):
    env_value = os.environ.get('USER_INPUT', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(env_value))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
