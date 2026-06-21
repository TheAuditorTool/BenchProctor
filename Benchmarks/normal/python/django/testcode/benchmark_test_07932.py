# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
from app_runtime import db


def BenchmarkTest07932(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
