# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
from app_runtime import db


def BenchmarkTest77723(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    importlib.import_module(str(db_value))
    return JsonResponse({"saved": True})
