# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest65835(request):
    user_id = request.GET.get('id', '')
    data = RequestPayload(user_id).value
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
