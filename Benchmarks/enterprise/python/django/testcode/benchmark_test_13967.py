# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest13967(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = RequestPayload(origin_value).value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
