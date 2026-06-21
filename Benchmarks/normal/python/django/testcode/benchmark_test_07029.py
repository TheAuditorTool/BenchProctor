# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def BenchmarkTest07029(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
