# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponseRedirect


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00251(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    return HttpResponseRedirect(str(data))
