# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00156(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    for _event, element in defusedxml.ElementTree.iterparse(io.BytesIO(str(data).encode()), events=('end',)):
        element.clear()
    return JsonResponse({"saved": True})
