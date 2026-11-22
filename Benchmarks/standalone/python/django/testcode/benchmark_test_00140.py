# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00140(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = RequestPayload(referer_value).value
    outbound = urllib.request.Request(str(data), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
