# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from urllib.parse import unquote
import os


def BenchmarkTest47881(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
