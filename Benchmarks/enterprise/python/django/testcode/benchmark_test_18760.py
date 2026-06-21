# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest18760(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = RequestPayload(json_value).value
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
