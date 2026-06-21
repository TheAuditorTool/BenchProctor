# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest61913(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
