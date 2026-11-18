# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00461(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = RequestPayload(origin_value).value
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
