# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest69830(request):
    host_value = request.META.get('HTTP_HOST', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
