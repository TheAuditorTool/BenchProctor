# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def BenchmarkTest09889(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
