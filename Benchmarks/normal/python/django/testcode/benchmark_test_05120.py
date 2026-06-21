# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest05120(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
