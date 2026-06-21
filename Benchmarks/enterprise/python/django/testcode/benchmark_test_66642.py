# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest66642(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
