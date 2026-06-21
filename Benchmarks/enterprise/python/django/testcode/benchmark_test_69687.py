# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest69687(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
