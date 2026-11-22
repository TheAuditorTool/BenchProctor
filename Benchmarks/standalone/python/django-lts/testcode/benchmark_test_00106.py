# SPDX-License-Identifier: Apache-2.0
import os
from django.http import HttpResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00106(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
