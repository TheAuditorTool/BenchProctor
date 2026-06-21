# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest07978(request):
    user_id = request.GET.get('id', '')
    data = RequestPayload(user_id).value
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
