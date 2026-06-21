# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest34578(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = db_value
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
