# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest70719(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
