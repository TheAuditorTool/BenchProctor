# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
from app_runtime import db


def BenchmarkTest66174(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(graphql_var),))
    logging.info('audit actor=%s action=revoke_sessions', str(graphql_var))
    return JsonResponse({"saved": True})
