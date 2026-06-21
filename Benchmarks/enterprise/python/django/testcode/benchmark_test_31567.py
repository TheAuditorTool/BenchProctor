# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest31567(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = RequestPayload(json_value).value
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
