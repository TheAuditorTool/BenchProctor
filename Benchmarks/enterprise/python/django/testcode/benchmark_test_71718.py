# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest71718(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
