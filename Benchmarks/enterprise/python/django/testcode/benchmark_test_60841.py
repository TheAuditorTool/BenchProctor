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

def BenchmarkTest60841(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
