# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest43068(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = RequestPayload(dotenv_value).value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
