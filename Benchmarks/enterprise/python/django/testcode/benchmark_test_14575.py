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

def BenchmarkTest14575(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
