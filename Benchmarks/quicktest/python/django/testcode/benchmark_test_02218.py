# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02218(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
