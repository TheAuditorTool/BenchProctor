# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest34623(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
