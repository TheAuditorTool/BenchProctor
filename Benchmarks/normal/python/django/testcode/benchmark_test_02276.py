# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import base64
from app_runtime import db


def BenchmarkTest02276(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
