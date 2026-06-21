# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


request_state: dict[str, str] = {}

def BenchmarkTest09626(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
