# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


request_state: dict[str, str] = {}

def BenchmarkTest02016(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
