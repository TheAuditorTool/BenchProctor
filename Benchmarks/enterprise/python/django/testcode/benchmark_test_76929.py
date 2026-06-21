# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest76929(request):
    user_id = request.GET.get('id', '')
    data = RequestPayload(user_id).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
