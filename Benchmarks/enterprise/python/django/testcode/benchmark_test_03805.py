# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest03805(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
