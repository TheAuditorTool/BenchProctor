# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest14842(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = RequestPayload(json_value).value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
