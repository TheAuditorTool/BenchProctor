# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00069(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = RequestPayload(cookie_value).value
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
