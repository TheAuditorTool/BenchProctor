# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest50103(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
