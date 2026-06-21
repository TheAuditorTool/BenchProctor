# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest43925(request):
    user_id = request.GET.get('id', '')
    data = RequestPayload(user_id).value
    int(str(data))
    return JsonResponse({"saved": True})
