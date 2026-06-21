# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest58480(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
