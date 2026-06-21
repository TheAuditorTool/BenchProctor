# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest44613(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
