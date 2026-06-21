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

def BenchmarkTest61017(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
