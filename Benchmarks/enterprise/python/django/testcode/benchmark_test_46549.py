# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest46549(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
