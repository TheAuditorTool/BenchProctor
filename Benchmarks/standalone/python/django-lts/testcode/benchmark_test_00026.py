# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00026(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = RequestPayload(forwarded_ip).value
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
