# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest00523(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = RequestPayload(db_value).value
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
