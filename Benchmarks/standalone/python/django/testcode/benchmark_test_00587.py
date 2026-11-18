# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00587(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
