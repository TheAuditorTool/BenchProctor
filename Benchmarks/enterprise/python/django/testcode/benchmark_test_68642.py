# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest68642(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
