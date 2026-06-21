# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse
import unicodedata


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest15097(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
