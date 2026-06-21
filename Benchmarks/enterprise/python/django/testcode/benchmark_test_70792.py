# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def relay_value(value):
    return value

def BenchmarkTest70792(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = relay_value(cookie_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
