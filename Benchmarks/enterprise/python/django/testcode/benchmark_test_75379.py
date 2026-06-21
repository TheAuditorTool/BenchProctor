# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import base64
from app_runtime import db


def BenchmarkTest75379(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
