# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def BenchmarkTest78495(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
