# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00062(request):
    upload_name = request.FILES['doc'].name
    data = RequestPayload(upload_name).value
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
