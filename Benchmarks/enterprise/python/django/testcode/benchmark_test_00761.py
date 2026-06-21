# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest00761(request):
    user_id = request.GET.get('id', '')
    data = RequestPayload(user_id).value
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
