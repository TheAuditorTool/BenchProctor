# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02105(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
