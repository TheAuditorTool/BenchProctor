# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from app_runtime import db


def BenchmarkTest12376(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
