# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64
from app_runtime import db


def BenchmarkTest50845(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
