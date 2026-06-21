# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest12706(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    logging.info('User action: ' + str(db_value))
    return JsonResponse({"saved": True})
