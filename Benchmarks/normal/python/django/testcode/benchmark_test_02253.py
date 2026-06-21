# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import json
import os


def BenchmarkTest02253(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
