# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest24251(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
