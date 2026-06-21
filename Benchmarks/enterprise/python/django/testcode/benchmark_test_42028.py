# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest42028(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = RequestPayload(auth_header).value
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
