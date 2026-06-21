# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from app_runtime import db


def BenchmarkTest36823(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
