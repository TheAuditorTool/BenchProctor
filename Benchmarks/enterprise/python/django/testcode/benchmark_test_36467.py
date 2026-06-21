# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest36467(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = RequestPayload(auth_header).value
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
