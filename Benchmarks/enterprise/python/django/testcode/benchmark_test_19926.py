# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import db


def BenchmarkTest19926(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    yaml.safe_load(db_value)
    return JsonResponse({"saved": True})
