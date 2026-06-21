# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import json
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest46111(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = coalesce_blank(json_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
