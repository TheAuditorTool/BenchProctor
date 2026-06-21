# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest60412(request):
    user_id = request.GET.get('id', '')
    data = RequestPayload(user_id).value
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
