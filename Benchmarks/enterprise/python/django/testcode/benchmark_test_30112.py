# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
from app_runtime import db


def BenchmarkTest30112(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
