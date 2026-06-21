# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys
from app_runtime import db


def BenchmarkTest80262(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
