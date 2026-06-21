# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02220(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = RequestPayload(auth_header).value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
