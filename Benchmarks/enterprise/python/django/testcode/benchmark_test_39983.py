# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def BenchmarkTest39983(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(db_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = db_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
