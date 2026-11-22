# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00002(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = RequestPayload(db_value).value
    parsed = json.JSONDecoder().decode(str(data))
    return JsonResponse({'parsed': str(parsed)}, status=200)
