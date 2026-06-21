# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03945(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
