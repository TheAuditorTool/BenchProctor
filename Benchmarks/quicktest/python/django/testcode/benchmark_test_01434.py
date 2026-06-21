# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest01434(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
