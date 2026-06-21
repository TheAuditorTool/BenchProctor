# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest10949(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
