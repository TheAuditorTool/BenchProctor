# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest13380(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
