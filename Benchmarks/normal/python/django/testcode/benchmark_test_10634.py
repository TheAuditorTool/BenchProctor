# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest10634(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
