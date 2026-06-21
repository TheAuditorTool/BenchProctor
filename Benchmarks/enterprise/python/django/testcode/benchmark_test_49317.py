# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest49317(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
