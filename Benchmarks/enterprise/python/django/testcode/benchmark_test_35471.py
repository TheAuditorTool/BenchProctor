# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest35471(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
