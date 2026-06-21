# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest55760(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
