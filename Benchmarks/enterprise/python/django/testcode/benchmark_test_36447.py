# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest36447(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
