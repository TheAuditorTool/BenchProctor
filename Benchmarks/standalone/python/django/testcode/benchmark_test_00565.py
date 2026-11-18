# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00565(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
