# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def BenchmarkTest31887(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
