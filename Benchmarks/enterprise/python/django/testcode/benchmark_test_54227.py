# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64
from app_runtime import db


def BenchmarkTest54227(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
