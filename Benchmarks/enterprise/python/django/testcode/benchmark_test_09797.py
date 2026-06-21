# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
from app_runtime import db


def BenchmarkTest09797(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
