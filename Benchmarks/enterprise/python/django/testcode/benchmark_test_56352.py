# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest56352(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
