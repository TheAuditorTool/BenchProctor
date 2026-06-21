# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest34745(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
