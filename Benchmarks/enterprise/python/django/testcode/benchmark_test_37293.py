# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def ensure_str(value):
    return str(value)

def BenchmarkTest37293(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
