# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import json
import os


def BenchmarkTest00863(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
