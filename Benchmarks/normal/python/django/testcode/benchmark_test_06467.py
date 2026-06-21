# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06467(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
