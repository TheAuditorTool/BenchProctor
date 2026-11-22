# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest00120(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
