# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest38567(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data = RequestPayload(query_array).value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
