# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest55854(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = RequestPayload(header_value).value
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
