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

def BenchmarkTest19391(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
