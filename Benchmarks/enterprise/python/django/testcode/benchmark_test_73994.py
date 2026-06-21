# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73994(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
