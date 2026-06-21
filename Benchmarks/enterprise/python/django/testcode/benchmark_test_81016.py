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

def BenchmarkTest81016(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
