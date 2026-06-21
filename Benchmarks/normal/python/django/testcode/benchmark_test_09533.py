# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09533(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
