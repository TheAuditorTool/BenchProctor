# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00058(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = RequestPayload(header_value).value
    Path('/var/app/data/' + str(data)).write_text('data')
    return JsonResponse({"saved": True})
