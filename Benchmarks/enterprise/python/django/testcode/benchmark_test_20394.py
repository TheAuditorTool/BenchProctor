# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest20394(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JsonResponse({'token': str(token)}, status=200)
