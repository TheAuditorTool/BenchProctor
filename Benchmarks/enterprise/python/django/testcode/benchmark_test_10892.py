# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest10892(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = RequestPayload(json_value).value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
