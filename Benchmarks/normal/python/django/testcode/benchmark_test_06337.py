# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest06337(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = RequestPayload(forwarded_ip).value
    requests.get(str(data))
    return JsonResponse({"saved": True})
