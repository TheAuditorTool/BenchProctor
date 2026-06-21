# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
from app_runtime import db


def BenchmarkTest39528(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(json_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(json_value))
    return JsonResponse({"saved": True})
